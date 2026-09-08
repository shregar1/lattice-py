"""Base abstraction for company repository service."""

from .abstraction import IAtomicRepositoryService


class ICompanyRepositoryService(IAtomicRepositoryService):
    """Marker base for company repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICompanyRepositoryService"
