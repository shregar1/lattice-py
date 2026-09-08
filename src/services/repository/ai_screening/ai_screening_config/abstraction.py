"""Base abstraction for ai_screening_config repository service."""

from .abstraction import IAtomicRepositoryService


class IAiScreeningConfigRepositoryService(IAtomicRepositoryService):
    """Marker base for ai_screening_config repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAiScreeningConfigRepositoryService"
