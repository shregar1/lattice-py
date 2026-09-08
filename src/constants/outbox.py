from typing import Final

from .abstraction import IConstant


class OutboxStatus(IConstant):

    PENDING: Final[str] = "PENDING"
    PUBLISHED: Final[str] = "PUBLISHED"
    FAILED: Final[str] = "FAILED"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "OutboxStatus"
