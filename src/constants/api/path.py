"""OpenAPI path constants for API endpoints."""

from typing import Final
from .abstraction import IAPIConstant


class APIPath(IAPIConstant):

    """Path constants for API endpoints."""

    API: Final[str] = "/api"
    V1: Final[str] = f"/v1"



    # Auth paths
    AUTH: Final[str] = f"auth"
    AUTH_LOGIN: Final[str] = f"login"
    AUTH_REGISTER: Final[str] = f"register"
    AUTH_LOGOUT: Final[str] = f"logout"

    # Health paths
    HEALTH: Final[str] = "/health"
    HEALTH_LIVENESS: Final[str] = "/liveness"
    HEALTH_READINESS: Final[str] = "/readiness"
    HEALTH_DB: Final[str] = "/db"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "APIPath"
