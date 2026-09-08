"""Base abstraction for ai_screening_criteria repository service."""

from .abstraction import IAtomicRepositoryService


class IAiScreeningCriteriaRepositoryService(IAtomicRepositoryService):
    """Marker base for ai_screening_criteria repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAiScreeningCriteriaRepositoryService"
