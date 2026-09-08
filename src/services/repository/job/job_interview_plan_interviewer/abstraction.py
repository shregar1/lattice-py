"""Base abstraction for job_interview_plan_interviewer repository service."""

from .abstraction import IAtomicRepositoryService


class IJobInterviewPlanInterviewerRepositoryService(IAtomicRepositoryService):
    """Marker base for job_interview_plan_interviewer repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobInterviewPlanInterviewerRepositoryService"
