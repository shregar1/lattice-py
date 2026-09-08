"""Base abstraction for ai_screening_run repository service."""

from .abstraction import IAtomicRepositoryService


class IAiScreeningRunRepositoryService(IAtomicRepositoryService):
    """Marker base for ai_screening_run repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAiScreeningRunRepositoryService"
