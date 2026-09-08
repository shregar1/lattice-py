from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.notification.abstraction import INotificationConfiguration
from constants import TeamsConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import TeamsConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class TeamsConfiguration(INotificationConfiguration):
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
        config_path: Optional[str] = TeamsConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        if config_path is None:
            logger.error("Config path is None")
            raise LoadConfigurationException(
                message="Config path is None",
            )

        INotificationConfiguration().__init__(
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
            logger=logger * args,
            **kwargs,
        )

    def validate(self, config: Dict[str, Any]) -> TeamsConfigurationDTO:

        try:
            return TeamsConfigurationDTO.build(
                webhook_url=config.get("webhook_url"),
                timeout_seconds=config.get("timeout_seconds", TeamsConfig.TIMEOUT_SECONDS),
                theme_color=config.get("theme_color", TeamsConfig.THEME_COLOR),
                title=config.get("title", TeamsConfig.TITLE),
                is_configured=config.get("is_configured", TeamsConfig.IS_CONFIGURED),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Teams configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Teams configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.TEAMS
