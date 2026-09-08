"""InternalServerException — raised for 500 Internal server error responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class InternalServerException(IException):
    """
    Internal server error exception (500).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.INTERNAL_SERVER
    status_code = HTTPStatus.INTERNAL_SERVER
    key = ExceptionKey.INTERNAL_SERVER

    def __init__(
        self,
        message: str = ExceptionMessage.INTERNAL_SERVER,
        **context: Any,
    ) -> None:
        """
        Initializes the InternalServerException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "InternalServerException"
