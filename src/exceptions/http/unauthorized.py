"""UnauthorizedException — raised for 401 Unauthorized responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class UnauthorizedException(IException):
    """
    Unauthorized exception (401).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.UNAUTHORIZED
    status_code = HTTPStatus.UNAUTHORIZED
    key = ExceptionKey.UNAUTHORIZED

    def __init__(
        self,
        message: str = ExceptionMessage.UNAUTHORIZED,
        **context: Any,
    ) -> None:
        """
        Initializes the UnauthorizedException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UnauthorizedException"
