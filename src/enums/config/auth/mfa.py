"""mfa enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import MFAConfig


class MFAConfigENUM(EnumLayer):
    CONFIG_PATH = MFAConfig.CONFIG_PATH
    ISSUER = MFAConfig.ISSUER
    TOTP_STEP_SECONDS = MFAConfig.TOTP_STEP_SECONDS
    TOTP_DIGITS = MFAConfig.TOTP_DIGITS
    RECOVERY_CODES_COUNT = MFAConfig.RECOVERY_CODES_COUNT
    RECOVERY_CODE_LENGTH = MFAConfig.RECOVERY_CODE_LENGTH
    OTP_EXPIRES_MINUTES = MFAConfig.OTP_EXPIRES_MINUTES
    MAX_ATTEMPTS = MFAConfig.MAX_ATTEMPTS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "MFAConfigENUM"

