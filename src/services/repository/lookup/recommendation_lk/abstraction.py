"""Base abstraction for recommendation_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IRecommendationLKRepositoryService(IAtomicRepositoryService):
    """Marker base for recommendation_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRecommendationLKRepositoryService"
