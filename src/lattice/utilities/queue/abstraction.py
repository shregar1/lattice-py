from abc import ABC, abstractmethod
from typing import Any, Callable

class BaseQueueClient(ABC):
    @abstractmethod
    async def publish(self, topic: str, payload: Any) -> str: pass
    @abstractmethod
    async def subscribe(self, topic: str, handler: Callable) -> None: pass
    @abstractmethod
    def get_driver_name(self) -> str: pass
