"""Base abstraction for model-layer dependency providers."""

from abc import abstractmethod

from ..abstraction import IModelDependency


class ILookupModelDependency(IModelDependency):
    """Marker base for all model-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        return "ILookupModelDependency"
