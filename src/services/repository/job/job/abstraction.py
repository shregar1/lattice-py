"""Base abstraction for job repository service."""

from .abstraction import IAtomicRepositoryService


class IJobRepositoryService(IAtomicRepositoryService):
    """Marker base for job repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobRepositoryService"
