"""Base abstraction for job_role_level_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IJobRoleLevelLKRepositoryService(IAtomicRepositoryService):
    """Marker base for job_role_level_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobRoleLevelLKRepositoryService"
