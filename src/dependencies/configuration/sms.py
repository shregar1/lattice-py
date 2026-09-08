from typing import Any
from .abstraction import ConfigurationLayerDependency
from rivex import Dependency

from constants import AppConfig
from constants import ConfigurationDependency
from configurations.sms import SMSConfiguration
from dependencies import LoggerUtilityDependency
from utilities import Logger


class SMSConfigurationDependency(ConfigurationLayerDependency):

    def resolve(
        self,
        urn: str = None,
        tenant_urn: str = None,
        user_urn: str = None,
        api_name: str = None,
        ip_address: str = None,
        user_agent: str = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        config_path: str = AppConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> SMSConfiguration:

        try:
            return SMSConfiguration(
                urn=urn,
                tenant_urn=tenant_urn,
                user_urn=user_urn,
                api_name=api_name,
                ip_address=ip_address,
                user_agent=user_agent,
                logger=logger,
                config_path=config_path,
                *args,
                **kwargs,
            )

        except Exception as exc:
            logger.error('Failed to resolve dependency', exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return ConfigurationDependency.SMS
