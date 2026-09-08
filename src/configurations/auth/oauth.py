from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.auth.abstraction import IAuthConfiguration
from constants import OAuthConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import OAuthConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class OAuthConfiguration(IAuthConfiguration):
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
        config_path: Optional[str] = OAuthConfig.CONFIG_PATH | None,
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

    def validate(self, config: Dict[str, Any]) -> OAuthConfigurationDTO:

        try:
            return OAuthConfigurationDTO.build(
                client_id=config.get("client_id"),
                client_secret=config.get("client_secret"),
                redirect_uri=config.get("redirect_uri", OAuthConfig.REDIRECT_URI),
                scopes=config.get("scopes"),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate OAuth configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate OAuth configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.OAUTH
