from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")
ID = TypeVar("ID")

class BaseRepository(ABC, Generic[T, ID]):
    """Base generic repository abstraction."""
    @abstractmethod
    async def find_by_id(self, id: ID) -> Optional[T]:
        pass
