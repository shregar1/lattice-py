"""Base abstraction for request-utility dependency providers."""

from abc import abstractmethod

from .abstraction import IDependency


class IRequestUtilityDependency(IDependency):
    """Marker base for all request-utility dependency providers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
