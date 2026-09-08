"""Postgres utility — asyncpg / ormx connection management and query helpers."""

import asyncpg
from typing import Any, List, Optional
from rivex import Dependency

from configurations.database.postgres import PostgresConfiguration, PostgresConfigurationDTO
from constants import Utility
from dependencies import PostgresConfigurationDependency
from dependencies import LoggerUtilityDependency
from .abstraction import IDatabaseUtility
from utilities import Logger


class PostgresDatabaseUtility(IDatabaseUtility):
    """Thin wrapper around an asyncpg pool with safe lifecycle helpers."""

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
        postgres_configuration: PostgresConfiguration = Dependency(PostgresConfigurationDependency),
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IDatabaseUtility.__init__(
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
            **kwargs,
        )
        self.postgres_configuration: PostgresConfigurationDTO = (
            postgres_configuration.get_instance()
        )
        self._pool = None

    async def connect(self) -> Any:
        """Open an asyncpg connection pool and return it."""
        try:
            self._pool = await asyncpg.create_pool(
                self.postgres_configuration.connection_uri,
                min_size=self.postgres_configuration.pool_min_size,
                max_size=self.postgres_configuration.pool_max_size,
            )
            return self._pool
        except ImportError:
            if self.logger is not None:
                self.logger.warning(
                    "asyncpg is not installed; PostgresDatabaseUtility will operate in disconnected mode"
                )
            self._pool = None
            return None

    async def disconnect(self) -> None:
        """Close the underlying asyncpg pool."""
        if self._pool is not None and hasattr(self._pool, "close"):
            await self._pool.close()
        self._pool = None

    async def fetch(self, query: str, *args: Any) -> List[Any]:
        """Run a SELECT and return all rows."""
        if self._pool is None:
            return []
        async with self._pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query: str, *args: Any) -> str:
        """Run a write query and return its status string."""
        if self._pool is None:
            return "SKIPPED"
        async with self._pool.acquire() as conn:
            return await conn.execute(query, *args)

    @property
    def pool(self) -> Any:
        return self._pool
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.POSTGRES_DATABASE
