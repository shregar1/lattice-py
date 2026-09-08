"""Base class for authentication configurations."""

from abc import abstractmethod

from abstractions import ConfigurationLayer


class IAuthConfiguration(ConfigurationLayer):
    """Base class for auth domain configuration layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
