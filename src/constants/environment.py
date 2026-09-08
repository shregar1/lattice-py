from typing import Final

from .abstraction import IConstant


class Environment(IConstant):

    DEVELOPMENT: Final[str] = "DEVELOPMENT"
    STAGING: Final[str] = "STAGING"
    PRODUCTION: Final[str] = "PRODUCTION"
    TESTING: Final[str] = "TESTING"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Environment"
