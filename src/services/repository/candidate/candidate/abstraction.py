"""Base abstraction for candidate repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateRepositoryService"
