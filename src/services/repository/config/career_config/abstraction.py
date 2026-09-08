"""Base abstraction for career_config repository service."""

from .abstraction import IAtomicRepositoryService


class ICareerConfigRepositoryService(IAtomicRepositoryService):
    """Marker base for career_config repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICareerConfigRepositoryService"
