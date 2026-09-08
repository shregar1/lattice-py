"""Response DTO layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class ResponseDTO(ILayerConstant):

    AUDIT_EVENT: Final[str] = "AuditEventResponseDTO"
    AUTH_TYPE_LK: Final[str] = "AuthTypeLKResponseDTO"
    USER: Final[str] = "UserResponseDTO"
    USER_OTP: Final[str] = "UserOtpResponseDTO"
    USER_RECOVERY_CODE: Final[str] = "UserRecoveryCodeResponseDTO"
    USER_TYPE_LK: Final[str] = "UserTypeLKResponseDTO"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ResponseDTO"
