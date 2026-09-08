from .abstraction import IConfigurationException
from constants import ExceptionCode, ExceptionKey
from constants import HTTPStatus


class LoadConfigurationException(IConfigurationException):
    def __init__(
        self,
        message: str = "Failed to load configuration",
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
        return "LoadConfigurationException"


__all__ = ["LoadConfigurationException"]
