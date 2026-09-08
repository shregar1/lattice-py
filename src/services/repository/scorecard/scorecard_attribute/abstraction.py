"""Base abstraction for scorecard_attribute repository service."""

from .abstraction import IAtomicRepositoryService


class IScorecardAttributeRepositoryService(IAtomicRepositoryService):
    """Marker base for scorecard_attribute repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IScorecardAttributeRepositoryService"
