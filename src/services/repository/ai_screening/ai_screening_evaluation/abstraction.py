"""Base abstraction for ai_screening_evaluation repository service."""

from .abstraction import IAtomicRepositoryService


class IAiScreeningEvaluationRepositoryService(IAtomicRepositoryService):
    """Marker base for ai_screening_evaluation repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAiScreeningEvaluationRepositoryService"
