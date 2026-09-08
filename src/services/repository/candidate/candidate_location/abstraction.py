"""Base abstraction for candidate_location repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateLocationRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate_location repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateLocationRepositoryService"
