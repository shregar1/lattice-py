"""OpenAPI endpoint summary constants."""

from typing import Final
from .abstraction import IAPIConstant


class APISummary(IAPIConstant):

    """Summary constants for API controller endpoints."""

    # Auth summaries
    USER_LOGIN: Final[str] = "User login"
    USER_REGISTRATION: Final[str] = "User registration"
    USER_LOGOUT: Final[str] = "User logout"

    # Health summaries
    LIVENESS_PROBE: Final[str] = "Liveness probe"
    READINESS_PROBE: Final[str] = "Readiness probe"
    DB_HEALTH_PROBE: Final[str] = "Database health probe"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "APISummary"
