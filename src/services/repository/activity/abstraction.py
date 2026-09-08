"""Base abstraction for activity repository service."""

from .abstraction import IAtomicRepositoryService


class IActivityRepositoryService(IAtomicRepositoryService):
    """Marker base for activity repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IActivityRepositoryService"
