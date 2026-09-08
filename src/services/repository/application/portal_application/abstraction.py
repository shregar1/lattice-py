"""Base abstraction for portal_application repository service."""

from .abstraction import IAtomicRepositoryService


class IPortalApplicationRepositoryService(IAtomicRepositoryService):
    """Marker base for portal_application repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IPortalApplicationRepositoryService"
