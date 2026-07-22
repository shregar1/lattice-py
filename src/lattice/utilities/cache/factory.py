import os
from lattice.utilities.cache.in_memory_driver import InMemoryCacheDriver
from lattice.utilities.cache.redis_driver import RedisCacheDriver

class CacheClientFactory:
    @staticmethod
    def create_client(config: dict = None):
        config = config or {}
        cache_type = config.get("type") or os.getenv("CACHE_TYPE", "in_memory")
        if cache_type.lower() == "redis": return RedisCacheDriver(config.get("redis"))
        return InMemoryCacheDriver()
