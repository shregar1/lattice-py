from typing import Final
from .abstraction import IHTTPConstant


class ResponseEntity(IHTTPConstant):

    STATUS: Final[str] = "status"
    BODY: Final[str] = "body"
    HEADERS: Final[str] = "headers"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ResponseEntity"
