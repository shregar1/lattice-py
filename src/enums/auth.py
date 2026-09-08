"""auth enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Auth


class AuthENUM(EnumLayer):
    OTP_LENGTH = Auth.OTP_LENGTH
    OTP_EXPIRY_MINUTES = Auth.OTP_EXPIRY_MINUTES
    MAX_LOGIN_ATTEMPTS = Auth.MAX_LOGIN_ATTEMPTS
    PASSWORD_MIN_LENGTH = Auth.PASSWORD_MIN_LENGTH

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "AuthENUM"

