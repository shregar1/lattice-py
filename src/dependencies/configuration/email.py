from typing import Any
from .abstraction import ConfigurationLayerDependency
from rivex import Dependency

from constants import EmailConfig
from constants import ConfigurationDependency
from configurations.email import EmailConfiguration
from dependencies import LoggerUtilityDependency
from utilities import Logger


class EmailConfigurationDependency(ConfigurationLayerDependency):

    def resolve(
        self,
        urn: str = None,
        tenant_urn: str = None,
        user_urn: str = None,
        api_name: str = None,
        ip_address: str = None,
        user_agent: str = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        config_path: str = EmailConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> EmailConfiguration:

        try:
            return EmailConfiguration(
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
        return ConfigurationDependency.EMAIL
