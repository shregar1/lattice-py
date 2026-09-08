"""ForbiddenException — raised for 403 Forbidden responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class ForbiddenException(IException):
    """
    Forbidden exception (403).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.FORBIDDEN
    status_code = HTTPStatus.FORBIDDEN
    key = ExceptionKey.FORBIDDEN

    def __init__(
        self,
        message: str = ExceptionMessage.FORBIDDEN,
        **context: Any,
    ) -> None:
        """
        Initializes the ForbiddenException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ForbiddenException"
