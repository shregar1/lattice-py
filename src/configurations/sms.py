from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from .abstraction import IConfiguration
from constants import SMSConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import SMSConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class SMSConfiguration(IConfiguration):

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
        config_path: Optional[str] = SMSConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        if config_path is None:
            logger.error("Config path is None")
            raise LoadConfigurationException(
                message="Config path is None",
            )

        IConfiguration.__init__(
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

    def validate(self, config: Dict[str, Any]) -> SMSConfigurationDTO:

        try:
            return SMSConfigurationDTO.build(
                from_number=config.get("from_number", SMSConfig.FROM_NUMBER),
                account_sid=config.get("account_sid", SMSConfig.ACCOUNT_SID),
                auth_token=config.get("auth_token", SMSConfig.AUTH_TOKEN),
                messaging_service_sid=config.get(
                    "messaging_service_sid", SMSConfig.MESSAGING_SERVICE_SID
                ),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate SMS configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate SMS configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.SMS
