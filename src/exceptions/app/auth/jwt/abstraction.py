"""Base class for JWT domain exceptions."""

from abc import abstractmethod

from .abstraction import IAuthException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class IJWTException(IAuthException):
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
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
