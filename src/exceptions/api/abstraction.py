"""Base class for API-layer exceptions."""

from .abstraction import IException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class IAPIException(IException):
    """Base exception for all API validation, bad input, and entity lookup errors."""

    def __init__(
        self,
        message: str = ExceptionMessage.BAD_INPUT,
        code: str = ExceptionCode.BAD_INPUT,
        key: str = ExceptionKey.BAD_INPUT,
        status_code: int = HTTPStatus.BAD_REQUEST,
    ) -> None:

        super().__init__(
            message=message,
            code=code,
            key=key,
            status_code=status_code,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAPIException"


__all__ = ["IAPIException"]
