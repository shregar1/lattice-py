"""Base class for authentication domain exceptions."""

from abc import abstractmethod

from .abstraction import IAppException


class IAuthException(IAppException):
    """Base exception for authentication domain errors."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
