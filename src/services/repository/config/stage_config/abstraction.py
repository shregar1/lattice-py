"""Base abstraction for stage_config repository service."""

from .abstraction import IAtomicRepositoryService


class IStageConfigRepositoryService(IAtomicRepositoryService):
    """Marker base for stage_config repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IStageConfigRepositoryService"
