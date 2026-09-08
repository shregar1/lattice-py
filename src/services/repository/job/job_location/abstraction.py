"""Base abstraction for job_location repository service."""

from .abstraction import IAtomicRepositoryService


class IJobLocationRepositoryService(IAtomicRepositoryService):
    """Marker base for job_location repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobLocationRepositoryService"
