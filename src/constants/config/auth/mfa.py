from typing import Final
from .abstraction import IConfigurationConstant


class MFAConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/auth/mfa/config.json"
    ISSUER: Final[str] = "mono"
    TOTP_STEP_SECONDS: Final[int] = 30
    TOTP_DIGITS: Final[int] = 6
    RECOVERY_CODES_COUNT: Final[int] = 10
    RECOVERY_CODE_LENGTH: Final[int] = 8
    OTP_EXPIRES_MINUTES: Final[int] = 5
    MAX_ATTEMPTS: Final[int] = 3

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "MFAConfig"
