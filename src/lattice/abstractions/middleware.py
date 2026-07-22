from abc import ABC, abstractmethod

class BaseMiddleware(ABC):
    """Base middleware stage abstraction."""
    @abstractmethod
    async def handle(self, request, call_next):
        pass
