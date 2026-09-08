from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.database.abstraction import IDatabaseConfiguration
from constants import MongoConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import MongoConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class MongoConfiguration(IDatabaseConfiguration):
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
        config_path: Optional[str] = MongoConfig.CONFIG_PATH,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        if config_path is None:
            logger.error("Config path is None")
            raise LoadConfigurationException(
                message="Config path is None",
            )

        super().__init__(
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

    def validate(self, config: Dict[str, Any]) -> MongoConfigurationDTO:

        try:
            return MongoConfigurationDTO.build(
                url=config.get("url"),
                database=config.get("database", MongoConfig.DATABASE),
                max_pool_size=config.get("max_pool_size", MongoConfig.MAX_POOL_SIZE),
                min_pool_size=config.get("min_pool_size", MongoConfig.MIN_POOL_SIZE),
                server_selection_timeout_ms=config.get(
                    "server_selection_timeout_ms", MongoConfig.SERVER_SELECTION_TIMEOUT_MS
                ),
                connect_timeout_ms=config.get("connect_timeout_ms", MongoConfig.CONNECT_TIMEOUT_MS),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Mongo configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Mongo configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.MONGO
