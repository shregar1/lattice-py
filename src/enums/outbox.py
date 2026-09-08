"""outbox enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import OutboxStatus


class OutboxStatusENUM(EnumLayer):
    PENDING = OutboxStatus.PENDING
    PUBLISHED = OutboxStatus.PUBLISHED
    FAILED = OutboxStatus.FAILED

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "OutboxStatusENUM"

