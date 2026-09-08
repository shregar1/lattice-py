"""Base abstraction for sourced_profile repository service."""

from .abstraction import IAtomicRepositoryService


class ISourcedProfileRepositoryService(IAtomicRepositoryService):
    """Marker base for sourced_profile repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISourcedProfileRepositoryService"
