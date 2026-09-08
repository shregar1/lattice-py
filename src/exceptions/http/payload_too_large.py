"""PayloadTooLargeException — raised for 413 Payload too large responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class PayloadTooLargeException(IException):
    """
    Payload too large exception (413).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.PAYLOAD_TOO_LARGE
    status_code = HTTPStatus.PAYLOAD_TOO_LARGE
    key = ExceptionKey.PAYLOAD_TOO_LARGE

    def __init__(
        self,
        message: str = ExceptionMessage.PAYLOAD_TOO_LARGE,
        **context: Any,
    ) -> None:
        """
        Initializes the PayloadTooLargeException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "PayloadTooLargeException"
