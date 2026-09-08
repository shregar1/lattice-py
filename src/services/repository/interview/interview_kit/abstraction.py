"""Base abstraction for interview_kit repository service."""

from .abstraction import IAtomicRepositoryService


class IInterviewKitRepositoryService(IAtomicRepositoryService):
    """Marker base for interview_kit repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IInterviewKitRepositoryService"
