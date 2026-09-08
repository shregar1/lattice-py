from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.auth.abstraction import IAuthConfiguration
from constants import MFAConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import MFAConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class MFAConfiguration(IAuthConfiguration):
    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        config_path: Optional[str] = MFAConfig.CONFIG_PATH | None,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        if config_path is None:
            logger.error("Config path is None")
            raise LoadConfigurationException(
                message="Config path is None",
            )

        IAuthConfiguration.__init__(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            config_path=config_path,
            *args,
            **kwargs,
        )

    def validate(self, config: Dict[str, Any]) -> MFAConfigurationDTO:

        try:
            return MFAConfigurationDTO.build(
                issuer=config.get("issuer", MFAConfig.ISSUER),
                totp_step_seconds=config.get("totp_step_seconds", MFAConfig.TOTP_STEP_SECONDS),
                totp_digits=config.get("totp_digits", MFAConfig.TOTP_DIGITS),
                recovery_codes_count=config.get(
                    "recovery_codes_count", MFAConfig.RECOVERY_CODES_COUNT
                ),
                recovery_code_length=config.get(
                    "recovery_code_length", MFAConfig.RECOVERY_CODE_LENGTH
                ),
                otp_expires_minutes=config.get(
                    "otp_expires_minutes", MFAConfig.OTP_EXPIRES_MINUTES
                ),
                max_attempts=config.get("max_attempts", MFAConfig.MAX_ATTEMPTS),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate MFA configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate MFA configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.MFA
