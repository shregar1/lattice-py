"""Base abstraction for scorecard repository service."""

from .abstraction import IAtomicRepositoryService


class IScorecardRepositoryService(IAtomicRepositoryService):
    """Marker base for scorecard repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IScorecardRepositoryService"
