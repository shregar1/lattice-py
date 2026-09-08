"""Base class for database configurations."""

from abc import abstractmethod

from abstractions import ConfigurationLayer


class IDatabaseConfiguration(ConfigurationLayer):
    """Base class for database domain configuration layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
