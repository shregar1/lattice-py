"""Authentication constants."""

from typing import Final

from .abstraction import IConstant


class Auth(IConstant):

    OTP_LENGTH: Final[int] = 6
    OTP_EXPIRY_MINUTES: Final[int] = 10
    MAX_LOGIN_ATTEMPTS: Final[int] = 5
    PASSWORD_MIN_LENGTH: Final[int] = 8

    DEFAULT_SCHEME: Final[str] = "bearer"
    SUBJECT_CLAIM: Final[str] = "sub"
    TENANT_CLAIM: Final[str] = "tenant_urn"
    USER_CLAIMS_KEY: Final[str] = "user_claims"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Auth"


AuthConstant = Auth

__all__ = ["Auth", "AuthConstant"]
