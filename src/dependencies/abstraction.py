"""Root abstraction for the dependency-injection layer."""

from abc import abstractmethod

from abstractions import DependencyLayer


class IDependency(DependencyLayer):
    """Marker base for all dependency providers across repository / services / utility layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
