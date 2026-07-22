from abc import ABC, abstractmethod

class BaseMigration(ABC):
    version: str
    name: str
    @abstractmethod
    async def up(self): pass
    @abstractmethod
    async def down(self): pass
