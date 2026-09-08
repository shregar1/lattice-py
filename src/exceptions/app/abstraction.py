"""Base class for application domain exceptions."""


from .abstraction import IException


class IAppException(IException):
    """Base exception for application-level domain errors."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return self.__class__.__name__

