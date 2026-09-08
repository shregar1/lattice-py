"""Base class for not found API exceptions."""

from .abstraction import IAPIException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class INotFoundException(IAPIException):
    def __init__(
        self,
        message: str = ExceptionMessage.NOT_FOUND,
        code: str = ExceptionCode.NOT_FOUND,
        key: str = ExceptionKey.NOT_FOUND,
        status_code: int = HTTPStatus.NOT_FOUND,
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
        return "INotFoundException"


__all__ = ["INotFoundException"]
