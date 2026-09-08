"""user_type enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import UserType


class UserTypeENUM(EnumLayer):
    SYSTEM_ADMIN = UserType.SYSTEM_ADMIN
    RECRUITER = UserType.RECRUITER
    INTERVIEWER = UserType.INTERVIEWER
    HIRING_MANAGER = UserType.HIRING_MANAGER
    CANDIDATE = UserType.CANDIDATE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "UserTypeENUM"

