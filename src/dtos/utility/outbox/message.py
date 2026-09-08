"""Persisted outbox-message DTO."""

import uuid

from datetime import datetime, timezone
from pydantic import Field
from typing import Optional, Self

from .abstraction import IOutBoxUtilityDTO


class OutboxMessage(IOutBoxUtilityDTO):
    """Persisted outbox row representing a domain event awaiting publication."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    aggregate_id: str
    payload_json: str
    status: str
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    published_at: Optional[str] = None

    @classmethod
    def build(
        cls,
        id: str,
        event_type: str,
        aggregate_id: str,
        payload_json: str,
        status: str,
        created_at: Optional[str] = None,
        published_at: Optional[str] = None,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            id=id,
            event_type=event_type,
            aggregate_id=aggregate_id,
            payload_json=payload_json,
            status=status,
            created_at=created_at,
            published_at=published_at,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "OutboxMessage"
