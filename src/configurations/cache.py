from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from .abstraction import IConfiguration
from constants import CacheConfig, Configuration
from dependencies import LoggerUtilityDependency
from dtos import CacheConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class CacheConfiguration(IConfiguration):

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
        config_path: Optional[str] = CacheConfig.CONFIG_PATH,
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

    def validate(self, config: Dict[str, Any]) -> CacheConfigurationDTO:

        try:
            return CacheConfigurationDTO.build(
                url=config.get("url"),
                max_connections=config.get("max_connections", CacheConfig.MAX_CONNECTIONS),
                socket_timeout=config.get("socket_timeout", CacheConfig.SOCKET_TIMEOUT),
                socket_connect_timeout=config.get(
                    "socket_connect_timeout", CacheConfig.SOCKET_CONNECT_TIMEOUT
                ),
                ttl_seconds=config.get("ttl_seconds", CacheConfig.TTL_SECONDS),
                key_prefix=config.get("key_prefix", CacheConfig.KEY_PREFIX),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Cache configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Cache configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.CACHE
