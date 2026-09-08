"""Repository dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class RepositoryDependency(ILayerConstant):

    AUDIT_EVENT: Final[str] = "AuditEventRepository"
    AUTH_TYPE_LK: Final[str] = "AuthTypeLKRepository"
    USER: Final[str] = "UserRepository"
    USER_OTP: Final[str] = "UserOtpRepository"
    USER_RECOVERY_CODE: Final[str] = "UserRecoveryCodeRepository"
    USER_TYPE_LK: Final[str] = "UserTypeLKRepository"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RepositoryDependency"
