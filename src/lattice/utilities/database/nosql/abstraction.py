from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict

class BaseDocumentDatabaseDriver(ABC):
    @abstractmethod
    async def connect(self) -> None: pass
    @abstractmethod
    async def disconnect(self) -> None: pass
    @abstractmethod
    async def insert_document(self, collection: str, doc: Dict[str, Any]) -> str: pass
    @abstractmethod
    async def find_document_by_id(self, collection: str, id: str) -> Optional[Dict[str, Any]]: pass
    @abstractmethod
    async def find_documents(self, collection: str, filter: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]: pass
    @abstractmethod
    async def update_document(self, collection: str, id: str, update: Dict[str, Any]) -> bool: pass
    @abstractmethod
    async def delete_document(self, collection: str, id: str) -> bool: pass
    @abstractmethod
    def get_driver_name(self) -> str: pass
