"""Base class for configuration domain exceptions."""

from abc import abstractmethod

from .abstraction import IAppException
from constants import ExceptionCode, ExceptionKey, ExceptionMessage
from constants import HTTPStatus


class IConfigurationException(IAppException):
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
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
