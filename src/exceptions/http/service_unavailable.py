"""ServiceUnavailableException — raised for 503 Service unavailable responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class ServiceUnavailableException(IException):
    """
    Service unavailable exception (503).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.SERVICE_UNAVAILABLE
    status_code = HTTPStatus.SERVICE_UNAVAILABLE
    key = ExceptionKey.SERVICE_UNAVAILABLE

    def __init__(
        self,
        message: str = ExceptionMessage.SERVICE_UNAVAILABLE,
        **context: Any,
    ) -> None:
        """
        Initializes the ServiceUnavailableException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ServiceUnavailableException"
