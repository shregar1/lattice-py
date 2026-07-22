from abc import ABC, abstractmethod
from typing import Any, List, Optional

class BaseDatabaseDriver(ABC):
    """Base database driver abstraction. Extend to implement MySQL, SQL Server, etc."""
    @abstractmethod
    async def connect(self) -> None: pass
    @abstractmethod
    async def disconnect(self) -> None: pass
    @abstractmethod
    async def query(self, sql: str, params: Optional[List[Any]] = None) -> List[Any]: pass
    @abstractmethod
    async def begin_transaction(self) -> Any: pass
    @abstractmethod
    async def health_check(self) -> bool: pass
    @abstractmethod
    def get_driver_name(self) -> str: pass
