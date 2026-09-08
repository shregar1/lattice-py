from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from .abstraction import IConfiguration
from constants import EmailConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import EmailConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class EmailConfiguration(IConfiguration):

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
        config_path: Optional[str] = EmailConfig.CONFIG_PATH,
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

    def validate(self, config: Dict[str, Any]) -> EmailConfigurationDTO:

        try:
            return EmailConfigurationDTO.build(
                email_from=config.get("email_from", EmailConfig.FROM),
                smtp_host=config.get("smtp_host", EmailConfig.SMTP_HOST),
                smtp_port=config.get("smtp_port", EmailConfig.SMTP_PORT),
                smtp_username=config.get("smtp_username", EmailConfig.SMTP_USERNAME),
                smtp_password=config.get("smtp_password", EmailConfig.SMTP_PASSWORD),
                smtp_use_tls=config.get("smtp_use_tls", EmailConfig.SMTP_USE_TLS),
                is_configured=config.get("is_configured", EmailConfig.IS_CONFIGURED),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Email configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Email configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.EMAIL
