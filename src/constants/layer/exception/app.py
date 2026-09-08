"""App exception layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class AppException(ILayerConstant):

    CONFIGURATION: Final[str] = "ConfigurationException"
    EXPIRED_TOKEN: Final[str] = "ExpiredTokenException"
    INVALID_TOKEN: Final[str] = "InvalidTokenException"
    JWT: Final[str] = "JWTException"
    VALIDATION: Final[str] = "ValidationException"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "AppException"
