from abc import ABC, abstractmethod
from typing import Any, Optional

class BaseCacheClient(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]: pass
    @abstractmethod
    async def set(self, key: str, value: Any, ttl_seconds: int = 3600) -> None: pass
    @abstractmethod
    async def delete(self, key: str) -> bool: pass
    @abstractmethod
    async def clear(self) -> None: pass
    @abstractmethod
    def get_driver_name(self) -> str: pass
