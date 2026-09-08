"""ConflictException — raised for 409 Conflict responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class ConflictException(IException):
    """
    Conflict exception (409).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.CONFLICT
    status_code = HTTPStatus.CONFLICT
    key = ExceptionKey.CONFLICT

    def __init__(
        self,
        message: str = ExceptionMessage.CONFLICT,
        **context: Any,
    ) -> None:
        """
        Initializes the ConflictException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ConflictException"
