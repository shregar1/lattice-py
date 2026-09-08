"""Base class for request utilities."""

from abc import abstractmethod

from .abstraction import IUtility


class IRequestUtility(IUtility):
    """Base class for request domain utility layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
