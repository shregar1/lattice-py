"""Base abstraction for candidate_tag repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateTagRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate_tag repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateTagRepositoryService"
