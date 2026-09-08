"""BadInputException — raised when client input fails validation."""

from typing import Any, Optional
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class BadInputException(IException):
    """
    Raised when the request body or parameters are syntactically invalid.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
        field: Optional name of the field that triggered the failure.
    """

    code = ExceptionCode.VALIDATION_ERROR
    status_code = HTTPStatus.BAD_REQUEST
    key = ExceptionKey.VALIDATION

    def __init__(
        self,
        message: str = ExceptionMessage.VALIDATION,
        field: Optional[str] = None,
        **context: Any,
    ) -> None:
        """
        Initializes the exception with the validation message and offending field.
        Args:
            message: Human-readable error message.
            field: Optional name of the field that triggered the failure.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)
        self.field = field

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "BadInputException"
