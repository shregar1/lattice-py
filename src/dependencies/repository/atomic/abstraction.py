"""Base abstraction for atomic repository-layer dependency providers."""

from abc import abstractmethod

from ..abstraction import IRepositoryDependency


class IAtomicRepositoryDependency(IRepositoryDependency):
    """Marker base for atomic repository-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "IAtomicRepositoryDependency"
