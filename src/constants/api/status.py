from typing import Final
from .abstraction import IAPIConstant


class ApiStatus(IAPIConstant):

    OK: Final[str] = "OK"
    SUCCESS: Final[str] = "SUCCESS"
    FAILED: Final[str] = "FAILED"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ApiStatus"
