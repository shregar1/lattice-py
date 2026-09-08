import json
from rivex import Dependency
from typing import Any, Optional

from constants import Utility
from dependencies import CacheConfigurationDependency
from dependencies import LoggerUtilityDependency
from configurations.cache import CacheConfiguration
from utilities import Logger
from .abstraction import IUtility


class RedisUtility(IUtility):
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
        cache_configuration: CacheConfiguration = Dependency(CacheConfigurationDependency),
        redis_client: Any = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IUtility.__init__(
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
            *args,
            **kwargs,
        )

        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.logger=logger
        self.cache_configuration = cache_configuration
        self.redis_client = redis_client
        self._memory_store: dict[str, str] = {}

    def _key(self, key: str) -> str:
        return f"{self.cache_configuration.prefix}{key}"

    async def get(self, key: str) -> Any | None:
        full_key = self._key(key=key)

        if self.redis_client is not None:
            try:
                val = await self.redis_client.get(name=full_key)
                return json.loads(val) if val else None
            except Exception:
                pass

        val_str = self._memory_store.get(key=full_key)
        return json.loads(val_str) if val_str else None

    async def set(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        full_key = self._key(key=key)
        serialized = json.dumps(value)

        if self.redis_client is not None:
            try:
                await self.redis_client.set(name=full_key, value=serialized, ex=ttl_seconds)
                return
            except Exception:
                pass

        self._memory_store[full_key] = serialized

    async def delete(self, key: str) -> None:
        full_key = self._key(key=key)

        if self.redis_client is not None:
            try:
                await self.redis_client.delete(names=full_key)
                return
            except Exception:
                pass

        self._memory_store.pop(key=full_key, default=None)

    async def clear(self) -> None:
        if self.redis_client is not None:
            try:
                await self.redis_client.flushdb()
                return
            except Exception:
                pass

        self._memory_store.clear()

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.REDIS
