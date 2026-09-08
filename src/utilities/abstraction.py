"""Base class for general utility layers."""

from abc import abstractmethod

from abstractions.utility import UtilityLayer


class IUtility(UtilityLayer):
    """Base class for utility domain layers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
