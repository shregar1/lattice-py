"""Base abstraction for integration repository service."""

from .abstraction import IAtomicRepositoryService


class IIntegrationRepositoryService(IAtomicRepositoryService):
    """Marker base for integration repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IIntegrationRepositoryService"
