from abc import ABC, abstractmethod

class BaseFactory(ABC):
    """Base factory abstraction."""
    @abstractmethod
    def create(self, *args, **kwargs):
        pass
