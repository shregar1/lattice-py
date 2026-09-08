"""Base abstraction for tenant repository service."""

from .abstraction import IAtomicRepositoryService


class ITenantRepositoryService(IAtomicRepositoryService):
    """Marker base for tenant repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITenantRepositoryService"
