from typing import Any, Dict, Self

from .abstraction import IDTO


class HTTPResponse(IDTO):
    status: int
    headers: Dict[str, Any]
    body: Dict[str, Any]

    @classmethod
    def build(cls, status: int, headers: Dict[str, Any], body: Dict[str, Any]) -> Self:
        """
        Method to ....
        """
        return cls(status=status, headers=headers, body=body)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HTTPResponse"
