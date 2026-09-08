"""Base abstraction for job_role repository service."""

from .abstraction import IAtomicRepositoryService


class IJobRoleRepositoryService(IAtomicRepositoryService):
    """Marker base for job_role repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobRoleRepositoryService"
