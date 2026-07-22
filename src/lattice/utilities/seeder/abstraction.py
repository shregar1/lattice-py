from abc import ABC, abstractmethod

class BaseSeeder(ABC):
    name: str
    @abstractmethod
    async def seed(self): pass
