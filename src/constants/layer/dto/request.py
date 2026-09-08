"""Request DTO layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class RequestDTO(ILayerConstant):

    AUDIT_EVENT: Final[str] = "AuditEventRequestDTO"
    AUTH_TYPE_LK: Final[str] = "AuthTypeLKRequestDTO"
    USER: Final[str] = "UserRequestDTO"
    USER_OTP: Final[str] = "UserOtpRequestDTO"
    USER_RECOVERY_CODE: Final[str] = "UserRecoveryCodeRequestDTO"
    USER_TYPE_LK: Final[str] = "UserTypeLKRequestDTO"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestDTO"
