from .abstraction import IOAuthException
from constants import ExceptionCode, ExceptionKey
from constants import HTTPStatus


class InvalidOAuthGrantException(IOAuthException):
    def __init__(
        self,
        message: str = "Invalid OAuth grant or authorization code",
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
        return "InvalidOAuthGrantException"


__all__ = ["InvalidOAuthGrantException"]
