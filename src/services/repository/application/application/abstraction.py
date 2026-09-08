"""Base abstraction for application repository service."""

from .abstraction import IAtomicRepositoryService


class IApplicationRepositoryService(IAtomicRepositoryService):
    """Marker base for application repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IApplicationRepositoryService"
