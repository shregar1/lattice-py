"""Model dependency layer constants."""

from typing import Final

from constants.layer.abstraction import ILayerConstant


class ModelDependency(ILayerConstant):

    AUDIT_EVENT: Final[str] = "AuditEventDependency"
    AUTH_TYPE_LK: Final[str] = "AuthTypeLKDependency"
    USER: Final[str] = "UserDependency"
    USER_OTP: Final[str] = "UserOtpDependency"
    USER_RECOVERY_CODE: Final[str] = "UserRecoveryCodeDependency"
    USER_TYPE_LK: Final[str] = "UserTypeLKDependency"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ModelDependency"
