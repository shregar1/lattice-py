"""Base abstraction for interview_interviewer repository service."""

from .abstraction import IAtomicRepositoryService


class IInterviewInterviewerRepositoryService(IAtomicRepositoryService):
    """Marker base for interview_interviewer repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IInterviewInterviewerRepositoryService"
