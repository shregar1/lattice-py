"""summary enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import APISummary


class APISummaryENUM(EnumLayer):
    USER_LOGIN = APISummary.USER_LOGIN
    USER_REGISTRATION = APISummary.USER_REGISTRATION
    USER_LOGOUT = APISummary.USER_LOGOUT
    LIVENESS_PROBE = APISummary.LIVENESS_PROBE
    READINESS_PROBE = APISummary.READINESS_PROBE
    DB_HEALTH_PROBE = APISummary.DB_HEALTH_PROBE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "APISummaryENUM"

