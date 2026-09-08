from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Dict, Optional

from configurations.notification.abstraction import INotificationConfiguration
from constants import SlackConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import SlackConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class SlackConfiguration(INotificationConfiguration):
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
        config_path: Optional[str] = SlackConfig.CONFIG_PATH,
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
            logger=logger,
            *args,
            **kwargs,
        )

    def validate(self, config: Dict[str, Any]) -> SlackConfigurationDTO:

        try:
            return SlackConfigurationDTO.build(
                webhook_url=config.get("webhook_url"),
                default_channel=config.get("default_channel", SlackConfig.DEFAULT_CHANNEL),
                username=config.get("username", SlackConfig.USERNAME),
                icon_emoji=config.get("icon_emoji", SlackConfig.ICON_EMOJI),
                timeout_seconds=config.get("timeout_seconds", SlackConfig.TIMEOUT_SECONDS),
                is_configured=config.get("is_configured", SlackConfig.IS_CONFIGURED),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Slack configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Slack configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.SLACK
