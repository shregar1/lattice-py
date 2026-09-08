"""Base abstraction for authentication orchestrators."""

from abstractions import IOrchestrator


class IAuthOrchestrator(IOrchestrator):
    """Marker base for all orchestrators in the auth domain under v1 API."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAuthOrchestrator"
