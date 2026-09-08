import asyncio
import json

from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any, List, Optional, Self

from constants import Utility, OutboxStatus
from dtos import OutBoxDomainEvent
from dtos import OutboxMessage
from .abstraction import IUtility


class OutboxUtility(IUtility):
    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        message_publisher: Callable[[OutboxMessage], Any] | None = None,
        poll_interval_seconds: float = 1.0,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        IUtility.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            *args,
            **kwargs,
        )
        self._outbox_queue: List[OutboxMessage] = []
        self._pending_worker_queue: List[OutboxMessage] = []
        self._publisher = message_publisher or self._default_publisher
        self.poll_interval = poll_interval_seconds
        self._in_transaction = False
        self._worker_running = False

    async def __aenter__(self) -> Self:
        self._in_transaction = True
        self._outbox_queue.clear()
        return self

    async def __aexit__(
        self, exc_type: type | None, exc_val: Exception | None, exc_tb: Any
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        self._in_transaction = False

    def record_event(self, event: OutBoxDomainEvent) -> OutboxMessage:
        outbox_msg = OutboxMessage(
            id=event.event_id,
            event_type=event.event_type,
            aggregate_id=event.aggregate_id,
            payload_json=json.dumps(event.payload),
        )
        self._outbox_queue.append(outbox_msg)
        return outbox_msg

    async def commit(self) -> None:
        if not self._in_transaction:
            return
        for msg in list(self._outbox_queue):
            try:
                await self._dispatch_message(msg)
                msg.status = OutboxStatus.PUBLISHED
                msg.published_at = datetime.now(timezone.utc).isoformat()
            except Exception:
                msg.status = OutboxStatus.FAILED
        self._outbox_queue.clear()

    async def rollback(self) -> None:
        self._outbox_queue.clear()

    async def _dispatch_message(self, message: OutboxMessage) -> None:
        if callable(self._publisher):
            res = self._publisher(message)
            if res is not None and hasattr(res, "__await__"):
                await res

    @staticmethod
    def _default_publisher(message: OutboxMessage) -> None:
        pass

    def enqueue(self, message: OutboxMessage) -> None:
        if message.status == OutboxStatus.PENDING:
            self._pending_worker_queue.append(message)

    async def process_batch(self) -> int:
        processed = 0
        batch = list(self._pending_worker_queue)
        self._pending_worker_queue.clear()
        for msg in batch:
            try:
                await self._dispatch_message(msg)
                msg.status = OutboxStatus.PUBLISHED
                msg.published_at = datetime.now(timezone.utc).isoformat()
                processed += 1
            except Exception:
                msg.status = OutboxStatus.FAILED
        return processed

    async def start_worker(self) -> None:
        self._worker_running = True
        while self._worker_running:
            await self.process_batch()
            await asyncio.sleep(self.poll_interval)

    def stop_worker(self) -> None:
        self._worker_running = False
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.OUTBOX
