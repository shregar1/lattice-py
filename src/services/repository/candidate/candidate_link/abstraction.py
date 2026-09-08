"""Base abstraction for candidate_link repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateLinkRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate_link repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateLinkRepositoryService"
