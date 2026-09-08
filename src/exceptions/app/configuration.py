from .abstraction import IAppException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class ConfigurationException(IAppException):
    def __init__(
        self,
        message: str = ExceptionMessage.INTERNAL_SERVER,
        code: str = ExceptionCode.INTERNAL_SERVER,
        key: str = ExceptionKey.INTERNAL_SERVER,
        status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,
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
        return "ConfigurationException"


__all__ = ["ConfigurationException"]
