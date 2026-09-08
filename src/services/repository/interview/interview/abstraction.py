"""Base abstraction for interview repository service."""

from .abstraction import IAtomicRepositoryService


class IInterviewRepositoryService(IAtomicRepositoryService):
    """Marker base for interview repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IInterviewRepositoryService"
