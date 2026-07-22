from lattice.utilities.database.nosql.abstraction import BaseDocumentDatabaseDriver

class InMemoryDocumentDriver(BaseDocumentDatabaseDriver):
    def __init__(self): self._store = {}
    async def connect(self) -> None: pass
    async def disconnect(self) -> None: pass
    async def insert_document(self, collection: str, doc: dict) -> str: return "doc_123"
    async def find_document_by_id(self, collection: str, id: str): return None
    async def find_documents(self, collection: str, filter = None): return []
    async def update_document(self, collection: str, id: str, update: dict) -> bool: return True
    async def delete_document(self, collection: str, id: str) -> bool: return True
    def get_driver_name(self) -> str: return "in_memory_doc"
