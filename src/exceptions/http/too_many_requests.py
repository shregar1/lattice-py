"""TooManyRequestsException — raised for 429 Too many requests responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class TooManyRequestsException(IException):
    """
    Too many requests exception (429).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.TOO_MANY_REQUESTS
    status_code = HTTPStatus.TOO_MANY_REQUESTS
    key = ExceptionKey.TOO_MANY_REQUESTS

    def __init__(
        self,
        message: str = ExceptionMessage.TOO_MANY_REQUESTS,
        **context: Any,
    ) -> None:
        """
        Initializes the TooManyRequestsException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TooManyRequestsException"
