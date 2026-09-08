"""Base class for application-wide constant containers."""

from abc import ABC, abstractmethod


class ConstantLayer(ABC):
    """Marker base for modules that only expose class-level constants."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
