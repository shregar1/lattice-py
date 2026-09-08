"""BadGatewayException — raised for 502 Bad gateway responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class BadGatewayException(IException):
    """
    Bad gateway exception (502).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_GATEWAY
    status_code = HTTPStatus.BAD_GATEWAY
    key = ExceptionKey.BAD_GATEWAY

    def __init__(
        self,
        message: str = ExceptionMessage.BAD_GATEWAY,
        **context: Any,
    ) -> None:
        """
        Initializes the BadGatewayException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "BadGatewayException"
