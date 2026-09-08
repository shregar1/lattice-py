"""path enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import APIPath


class APIPathENUM(EnumLayer):
    API = APIPath.API
    V1 = APIPath.V1
    AUTH = APIPath.AUTH
    AUTH_LOGIN = APIPath.AUTH_LOGIN
    AUTH_REGISTER = APIPath.AUTH_REGISTER
    AUTH_LOGOUT = APIPath.AUTH_LOGOUT
    HEALTH = APIPath.HEALTH
    HEALTH_LIVENESS = APIPath.HEALTH_LIVENESS
    HEALTH_READINESS = APIPath.HEALTH_READINESS
    HEALTH_DB = APIPath.HEALTH_DB

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "APIPathENUM"

