"""Base class for OAuth domain exceptions."""

from .abstraction import IAuthException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class IOAuthException(IAuthException):
    def __init__(
        self,
        message: str = ExceptionMessage.UNAUTHORIZED,
        code: str = ExceptionCode.UNAUTHORIZED,
        key: str = ExceptionKey.UNAUTHORIZED,
        status_code: int = HTTPStatus.UNAUTHORIZED,
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
        return "IOAuthException"


__all__ = ["IOAuthException"]
