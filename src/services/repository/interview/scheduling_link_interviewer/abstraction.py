"""Base abstraction for scheduling_link_interviewer repository service."""

from .abstraction import IAtomicRepositoryService


class ISchedulingLinkInterviewerRepositoryService(IAtomicRepositoryService):
    """Marker base for scheduling_link_interviewer repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISchedulingLinkInterviewerRepositoryService"
