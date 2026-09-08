from typing import Any
from rivex import Dependency

from .abstraction import IAuthConfigurationDependency
from constants import JWTConfig
from constants import ConfigurationDependency
from configurations.auth.jwt import JWTConfiguration
from dependencies import LoggerUtilityDependency
from utilities import Logger


class JWTConfigurationDependency(IAuthConfigurationDependency):

    def resolve(
        self,
        urn: str = None,
        tenant_urn: str = None,
        user_urn: str = None,
        api_name: str = None,
        ip_address: str = None,
        user_agent: str = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        config_path: str = JWTConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> JWTConfiguration:

        try:
            return JWTConfiguration(
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
        return ConfigurationDependency.JWT
