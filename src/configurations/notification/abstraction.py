"""Base class for notification configurations."""

from abc import abstractmethod

from abstractions import ConfigurationLayer


class INotificationConfiguration(ConfigurationLayer):
    """Base class for notification domain configuration layers."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
