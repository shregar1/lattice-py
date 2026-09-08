"""Base abstraction for ai_screening_status_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IAiScreeningStatusLKRepositoryService(IAtomicRepositoryService):
    """Marker base for ai_screening_status_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAiScreeningStatusLKRepositoryService"
