from .abstraction import IMFAException
from constants import ExceptionCode, ExceptionKey
from constants import HTTPStatus


class ExpiredMFASessionException(IMFAException):
    def __init__(
        self,
        message: str = "MFA session has expired",
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
        return "ExpiredMFASessionException"


__all__ = ["ExpiredMFASessionException"]
