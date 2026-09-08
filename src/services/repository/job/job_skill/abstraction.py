"""Base abstraction for job_skill repository service."""

from .abstraction import IAtomicRepositoryService


class IJobSkillRepositoryService(IAtomicRepositoryService):
    """Marker base for job_skill repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobSkillRepositoryService"
