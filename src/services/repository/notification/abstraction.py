"""Base abstraction for notification repository service."""

from .abstraction import IAtomicRepositoryService


class INotificationRepositoryService(IAtomicRepositoryService):
    """Marker base for notification repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "INotificationRepositoryService"
