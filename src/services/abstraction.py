"""Base abstraction for all application services."""

from abstractions import ServiceLayer


class IService(ServiceLayer):
    """Marker base for all services in the application."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IService"
