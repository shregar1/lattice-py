"""Base abstraction for dedup_group repository service."""

from .abstraction import IAtomicRepositoryService


class IDedupGroupRepositoryService(IAtomicRepositoryService):
    """Marker base for dedup_group repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDedupGroupRepositoryService"
