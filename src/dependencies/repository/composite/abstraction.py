"""Base abstraction for composite repository-layer dependency providers."""

from abc import abstractmethod

from ..abstraction import IRepositoryDependency


class ICompositeRepositoryDependency(IRepositoryDependency):
    """Marker base for composite repository-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "ICompositeRepositoryDependency"
