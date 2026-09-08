"""Base abstraction for dedup_group_candidate repository service."""

from .abstraction import IAtomicRepositoryService


class IDedupGroupCandidateRepositoryService(IAtomicRepositoryService):
    """Marker base for dedup_group_candidate repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDedupGroupCandidateRepositoryService"
