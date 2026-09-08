"""UnprocessableEntityException — raised when input is syntactically valid but semantically rejected."""

from typing import Any, Optional
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus
from .abstraction import IException


class UnprocessableEntityException(IException):
    """
    Raised when the request is well-formed but cannot be processed.
    The ``code`` and ``key`` may be overridden per-instance to surface
    the specific semantic reason without losing the 422 status.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.UNPROCESSABLE_ENTITY
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    key = ExceptionKey.UNPROCESSABLE_ENTITY

    def __init__(
        self,
        message: str = ExceptionMessage.UNPROCESSABLE_ENTITY,
        code: Optional[str] = None,
        key: Optional[str] = None,
        **context: Any,
    ) -> None:
        """
        Initializes the exception, optionally overriding ``code`` and ``key``.
        Args:
            message: Human-readable error message.
            code: Optional per-instance code override; falls back to the class default.
            key: Optional per-instance key override; falls back to the class default.
            **context: Additional structured fields attached to the exception.
        """
        super().__init__(
            message,
            code=code or self.code,
            key=key or self.key,
            status_code=self.status_code,
            **context,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UnprocessableEntityException"
