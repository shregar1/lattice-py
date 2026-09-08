"""environment enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Environment


class EnvironmentENUM(EnumLayer):
    DEVELOPMENT = Environment.DEVELOPMENT
    STAGING = Environment.STAGING
    PRODUCTION = Environment.PRODUCTION
    TESTING = Environment.TESTING

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "EnvironmentENUM"

