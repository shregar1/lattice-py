"""Base abstraction for job_interview_plan repository service."""

from .abstraction import IAtomicRepositoryService


class IJobInterviewPlanRepositoryService(IAtomicRepositoryService):
    """Marker base for job_interview_plan repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobInterviewPlanRepositoryService"
