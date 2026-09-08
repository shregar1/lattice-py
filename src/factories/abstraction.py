from abc import abstractmethod
from typing import Any

from abstractions import FactoryLayer


class IFactory(FactoryLayer):
    """Marker base for all factory-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "IFactory"