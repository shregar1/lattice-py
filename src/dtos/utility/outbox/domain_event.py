"""Domain-event DTO queued for the outbox."""

import uuid

from datetime import datetime, timezone
from pydantic import Field
from typing import Any, Dict, Self

from .abstraction import IOutBoxUtilityDTO


class OutBoxDomainEvent(IOutBoxUtilityDTO):
    """In-memory representation of a domain event queued for the outbox."""

    event_type: str
    aggregate_id: str
    payload: Dict[str, Any]
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    occurred_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    @classmethod
    def build(
        cls,
        event_type: str,
        aggregate_id: str,
        payload: Dict[str, Any],
        event_id: str,
        occurred_at: str,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            event_type=event_type,
            aggregate_id=aggregate_id,
            payload=payload,
            event_id=event_id,
            occurred_at=occurred_at,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "OutBoxDomainEvent"
