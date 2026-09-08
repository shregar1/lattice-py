"""GatewayTimeoutException — raised for 504 Gateway timeout responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class GatewayTimeoutException(IException):
    """
    Gateway timeout exception (504).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.GATEWAY_TIMEOUT
    status_code = HTTPStatus.GATEWAY_TIMEOUT
    key = ExceptionKey.GATEWAY_TIMEOUT

    def __init__(
        self,
        message: str = ExceptionMessage.GATEWAY_TIMEOUT,
        **context: Any,
    ) -> None:
        """
        Initializes the GatewayTimeoutException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "GatewayTimeoutException"
