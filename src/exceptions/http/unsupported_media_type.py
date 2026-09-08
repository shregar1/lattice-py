"""UnsupportedMediaTypeException — raised for 415 Unsupported media type responses."""

from typing import Any
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class UnsupportedMediaTypeException(IException):
    """
    Unsupported media type exception (415).
    Raised by controllers and services when the corresponding HTTP condition is met.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.UNSUPPORTED_MEDIA_TYPE
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    key = ExceptionKey.UNSUPPORTED_MEDIA_TYPE

    def __init__(
        self,
        message: str = ExceptionMessage.UNSUPPORTED_MEDIA_TYPE,
        **context: Any,
    ) -> None:
        """
        Initializes the UnsupportedMediaTypeException.
        Args:
            message: Human-readable error message.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(message, **context)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UnsupportedMediaTypeException"
