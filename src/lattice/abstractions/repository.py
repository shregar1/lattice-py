# Lattice (Python Edition) — Repository Abstraction
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Any, Dict

T = TypeVar("T")
ID = TypeVar("ID")

class IBaseRepository(ABC, Generic[T, ID]):
    """Standardized Lattice Repository Interface."""

    @abstractmethod
    async def find_by_id(self, id: ID) -> Optional[T]: pass

    @abstractmethod
    async def find_by_urn(self, urn: str) -> Optional[T]: pass

    @abstractmethod
    async def find_one(self, criteria: Dict[str, Any]) -> Optional[T]: pass

    @abstractmethod
    async def find_all(self, criteria: Optional[Dict[str, Any]] = None) -> List[T]: pass

    @abstractmethod
    async def find_paginated(self, criteria: Dict[str, Any]) -> Dict[str, Any]: pass

    @abstractmethod
    async def create(self, entity: T) -> T: pass

    @abstractmethod
    async def create_many(self, entities: List[T]) -> List[T]: pass

    @abstractmethod
    async def update(self, id: ID, entity: Dict[str, Any]) -> T: pass

    @abstractmethod
    async def update_many(self, criteria: Dict[str, Any], data: Dict[str, Any]) -> int: pass

    @abstractmethod
    async def delete(self, id: ID) -> bool: pass

    @abstractmethod
    async def soft_delete(self, id: ID) -> bool: pass

    @abstractmethod
    async def restore(self, id: ID) -> bool: pass

    @abstractmethod
    async def delete_many(self, criteria: Dict[str, Any]) -> int: pass

    @abstractmethod
    async def count(self, criteria: Optional[Dict[str, Any]] = None) -> int: pass

    @abstractmethod
    async def exists(self, criteria: Dict[str, Any]) -> bool: pass
