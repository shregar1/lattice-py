"""Base abstraction for utility-layer dependency providers."""

from abc import abstractmethod

from .abstraction import IDependency


class IUtilityDependency(IDependency):
    """Marker base for all utility-layer dependency providers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
