"""Base abstraction for database-utility dependency providers."""

from abc import abstractmethod

from .abstraction import IUtilityDependency


class IDatabaseUtilityDependency(IUtilityDependency):
    """Marker base for all database-utility dependency providers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
