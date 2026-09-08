"""Base abstraction for tenant_profile repository service."""

from .abstraction import IAtomicRepositoryService


class ITenantProfileRepositoryService(IAtomicRepositoryService):
    """Marker base for tenant_profile repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITenantProfileRepositoryService"
