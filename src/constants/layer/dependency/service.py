"""Service dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class ServiceDependency(ILayerConstant):

    AUDIT_EVENT: Final[str] = "AuditEventService"
    AUTH_TYPE_LK: Final[str] = "AuthTypeLKService"
    USER: Final[str] = "UserService"
    USER_OTP: Final[str] = "UserOtpService"
    USER_RECOVERY_CODE: Final[str] = "UserRecoveryCodeService"
    USER_TYPE_LK: Final[str] = "UserTypeLKService"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ServiceDependency"
