from .abstraction import IOAuthException
from constants import ExceptionCode, ExceptionKey
from constants import HTTPStatus


class OAuthProviderException(IOAuthException):
    def __init__(
        self,
        message: str = "OAuth provider communication error",
        code: str = ExceptionCode.BAD_GATEWAY,
        key: str = ExceptionKey.BAD_GATEWAY,
        status_code: int = HTTPStatus.BAD_GATEWAY,
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
        return "OAuthProviderException"


__all__ = ["OAuthProviderException"]
