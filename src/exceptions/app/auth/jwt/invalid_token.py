from .abstraction import IJWTException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class InvalidTokenException(IJWTException):
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
        return "InvalidTokenException"
