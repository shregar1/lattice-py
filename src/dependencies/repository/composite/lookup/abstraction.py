"""Base abstraction for composite repository-layer dependency providers."""

from abc import abstractmethod

from typing import Any

from ..abstraction import ICompositeRepositoryDependency


class ICompositeLookupRepositoryDependency(ICompositeRepositoryDependency):
    """Marker base for composite repository-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "ICompositeLookupRepositoryDependency"
