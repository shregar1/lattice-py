"""Base abstraction for background_check repository service."""

from .abstraction import IAtomicRepositoryService


class IBackgroundCheckRepositoryService(IAtomicRepositoryService):
    """Marker base for background_check repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IBackgroundCheckRepositoryService"
