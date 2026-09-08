"""Base class for database utilities."""

from abc import abstractmethod

from .abstraction import IUtility


class IDatabaseUtility(IUtility):
    """Base class for database domain utility layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""

        return "IDatabaseUtility"
