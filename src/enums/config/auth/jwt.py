"""jwt enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import JWTConfig


class JWTConfigENUM(EnumLayer):
    CONFIG_PATH = JWTConfig.CONFIG_PATH
    EXPIRES_MINUTES = JWTConfig.EXPIRES_MINUTES
    REFRESH_EXPIRES_DAYS = JWTConfig.REFRESH_EXPIRES_DAYS
    ALGORITHM = JWTConfig.ALGORITHM
    MIN_JWT_SECRET_LENGTH = JWTConfig.MIN_JWT_SECRET_LENGTH

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "JWTConfigENUM"

