"""Base abstraction for scheduling_link repository service."""

from .abstraction import IAtomicRepositoryService


class ISchedulingLinkRepositoryService(IAtomicRepositoryService):
    """Marker base for scheduling_link repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISchedulingLinkRepositoryService"
