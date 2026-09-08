"""Base abstraction for configuration-layer dependency providers."""

from abc import abstractmethod

from .abstraction import IDependency


class ConfigurationLayerDependency(IDependency):
    """Marker base for all configuration-layer dependency providers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
