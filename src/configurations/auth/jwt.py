from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.auth.abstraction import IAuthConfiguration
from constants import JWTConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import JWTConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class JWTConfiguration(IAuthConfiguration):
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
        config_path: Optional[str] = JWTConfig.CONFIG_PATH | None,
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

    def validate(self, config: Dict[str, Any]) -> JWTConfigurationDTO:

        try:
            return JWTConfigurationDTO.build(
                secret=config.get("secret"),
                refresh_secret=config.get("refresh_secret"),
                expires_minutes=config.get("expires_minutes", JWTConfig.EXPIRES_MINUTES),
                refresh_expires_days=config.get(
                    "refresh_expires_days", JWTConfig.REFRESH_EXPIRES_DAYS
                ),
                algorithm=config.get("algorithm", JWTConfig.ALGORITHM),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate JWT configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate JWT configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.JWT
