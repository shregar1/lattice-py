"""Base class for security/threat API exceptions."""

from .abstraction import IAPIException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class ISecurityException(IAPIException):
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
        return "ISecurityException"


__all__ = ["ISecurityException"]
