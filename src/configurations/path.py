from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from .abstraction import IConfiguration
from constants import PathConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import PathConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class PathConfiguration(IConfiguration):

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
        config_path: Optional[str] = PathConfig.CONFIG_PATH,
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

    def validate(self, config: Dict[str, Any]) -> PathConfigurationDTO:

        try:
            return PathConfigurationDTO.build(
                logs_dir=config.get("logs_dir", PathConfig.LOGS_DIR),
                migrations_dir=config.get("migrations_dir", PathConfig.MIGRATIONS_DIR),
                scripts_dir=config.get("scripts_dir", PathConfig.SCRIPTS_DIR),
                media_dir=config.get("media_dir", PathConfig.MEDIA_DIR),
                media_url_prefix=config.get("media_url_prefix", PathConfig.MEDIA_URL_PREFIX),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Paths configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Paths configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.PATH
