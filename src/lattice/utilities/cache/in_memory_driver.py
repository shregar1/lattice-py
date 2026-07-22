from lattice.utilities.cache.abstraction import BaseCacheClient

class InMemoryCacheDriver(BaseCacheClient):
    def __init__(self): self._store = {}
    async def get(self, key: str): return self._store.get(key)
    async def set(self, key: str, value: any, ttl_seconds: int = 3600): self._store[key] = value
    async def delete(self, key: str) -> bool: return self._store.pop(key, None) is not None
    async def clear(self) -> None: self._store.clear()
    def get_driver_name(self) -> str: return "in_memory"
