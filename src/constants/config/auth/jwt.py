from typing import Final
from .abstraction import IConfigurationConstant


class JWTConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/auth/jwt/config.json"
    EXPIRES_MINUTES: Final[int] = 15
    REFRESH_EXPIRES_DAYS: Final[int] = 7
    ALGORITHM: Final[str] = "HS256"
    MIN_JWT_SECRET_LENGTH: Final[int] = 32

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "JWTConfig"
