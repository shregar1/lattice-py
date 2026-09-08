from typing import Final

from .abstraction import IConstant


class JWT(IConstant):

    ACCESS: Final[str] = "access"
    REFRESH: Final[str] = "refresh"
    JTI: Final[str] = "JTI"
    HS256: Final[str] = "HS256"
    HS384: Final[str] = "HS384"
    HS512: Final[str] = "HS512"
    RS256: Final[str] = "RS256"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "JWT"
