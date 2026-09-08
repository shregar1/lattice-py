"""ValidationException — raised for 400 Validation error responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class ValidationException(IException):
    """
    Validation error exception (400).
    Duplicate of the non-suffixed variant kept for legacy imports.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.VALIDATION
    status_code = HTTPStatus.VALIDATION
    key = ExceptionKey.VALIDATION

    def __init__(
        self,
        message: str = ExceptionMessage.VALIDATION,
        **context: Any,
    ) -> None:
        """
        Initializes the ValidationException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ValidationException"
