"""MethodNotAllowedException — raised for 405 Method not allowed responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class MethodNotAllowedException(IException):
    """
    Method not allowed exception (405).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.METHOD_NOT_ALLOWED
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    key = ExceptionKey.METHOD_NOT_ALLOWED

    def __init__(
        self,
        message: str = ExceptionMessage.METHOD_NOT_ALLOWED,
        **context: Any,
    ) -> None:
        """
        Initializes the MethodNotAllowedException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "MethodNotAllowedException"
