"""Base abstraction for atomic repository-layer dependency providers."""

from abc import abstractmethod

from typing import Any

from ..abstraction import IAtomicRepositoryDependency


class IAtomicLookupRepositoryDependency(IAtomicRepositoryDependency):
    """Marker base for atomic repository-layer dependency providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        return "IAtomicLookupRepositoryDependency"
