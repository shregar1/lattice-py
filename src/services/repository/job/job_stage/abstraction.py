"""Base abstraction for job_stage repository service."""

from .abstraction import IAtomicRepositoryService


class IJobStageRepositoryService(IAtomicRepositoryService):
    """Marker base for job_stage repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobStageRepositoryService"
