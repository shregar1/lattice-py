from pydantic import ValidationError
from rivex import Dependency
from typing import Any, Optional, Dict

from configurations.database.abstraction import IDatabaseConfiguration
from constants import PostgresConfig
from constants import Configuration
from dependencies import LoggerUtilityDependency
from dtos import PostgresConfigurationDTO
from exceptions import LoadConfigurationException
from utilities import Logger


class PostgresConfiguration(IDatabaseConfiguration):
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
        config_path: Optional[str] = PostgresConfig.CONFIG_PATH,
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

    def validate(self, config: Dict[str, Any]) -> PostgresConfigurationDTO:

        try:
            return PostgresConfigurationDTO.build(
                host=config.get("host", PostgresConfig.HOST),
                port=config.get("port", PostgresConfig.PORT),
                database=config.get("database", PostgresConfig.DATABASE),
                user=config.get("user", PostgresConfig.USER),
                password=config.get("password"),
                schema=config.get("schema", PostgresConfig.SCHEMA),
                ssl_mode=config.get("ssl_mode", PostgresConfig.SSL_MODE),
                pool_size=config.get("pool_size", PostgresConfig.POOL_SIZE),
                max_overflow=config.get("max_overflow", PostgresConfig.MAX_OVERFLOW),
                pool_timeout=config.get("pool_timeout", PostgresConfig.POOL_TIMEOUT),
                pool_recycle=config.get("pool_recycle", PostgresConfig.POOL_RECYCLE),
                echo=config.get("echo", PostgresConfig.ECHO),
            )

        except ValidationError as exc:
            self.logger.error("Failed to validate Postgres configuration", exc=exc)
            raise exc

        except Exception as exc:
            self.logger.error("Failed to validate Postgres configuration", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""

        return Configuration.POSTGRES
