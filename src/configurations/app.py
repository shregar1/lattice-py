from pydantic import ValidationError
from typing import Any, Optional, Dict
from rivex import Dependency

from .abstraction import IConfiguration
from constants import AppConfig, Configuration
from dependencies import LoggerUtilityDependency
from dtos import AppConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class AppConfiguration(IConfiguration):

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
        config_path: Optional[str] = AppConfig.CONFIG_PATH | None,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        if config_path is None:
            logger.error("Config path is None")
            raise LoadConfigurationException(
                message="Config path is None",
            )

        IConfiguration.__init__(
            self,
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

    def validate(self, config: Dict[str, Any]) -> AppConfigurationDTO:

        try:
            return AppConfigurationDTO.build(
                name=config.get("name", AppConfig.NAME),
                powered_by=config.get("powered_by", AppConfig.POWERED_BY),
                host=config.get("host", AppConfig.HOST),
                port=config.get("port", AppConfig.PORT),
                cors_origin=config.get("cors_origin", ""),
                rate_limit_max=config.get("rate_limit_max", AppConfig.RATE_LIMIT_MAX),
                rate_limit_window_seconds=config.get(
                    "rate_limit_window_seconds", AppConfig.RATE_LIMIT_WINDOW_SECONDS
                ),
                debug=config.get("debug", AppConfig.DEBUG),
                request_timeout=config.get("request_timeout", AppConfig.REQUEST_TIMEOUT),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate App configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate App configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.APP
