from typing import Self

from .abstraction import IAuthConfigurationDTO
from constants import Configuration


class MFAConfigurationDTO(IAuthConfigurationDTO):
    issuer: str
    totp_step_seconds: int
    totp_digits: int
    recovery_codes_count: int
    recovery_code_length: int
    otp_expires_minutes: int
    max_attempts: int

    @classmethod
    def build(
        cls,
        issuer: str,
        totp_step_seconds: int,
        totp_digits: int,
        recovery_codes_count: int,
        recovery_code_length: int,
        otp_expires_minutes: int,
        max_attempts: int,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            issuer=issuer,
            totp_step_seconds=totp_step_seconds,
            totp_digits=totp_digits,
            recovery_codes_count=recovery_codes_count,
            recovery_code_length=recovery_code_length,
            otp_expires_minutes=otp_expires_minutes,
            max_attempts=max_attempts,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.MFA
