"""Base abstraction for composite repository-layer dependency providers."""

from abc import abstractmethod

from typing import Any

from ..abstraction import IDependency


class IRepositoryDependency(IDependency):
    """Marker base for repository-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "IRepositoryDependency"
