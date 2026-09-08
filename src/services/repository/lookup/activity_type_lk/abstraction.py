"""Base abstraction for activity_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IActivityTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for activity_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IActivityTypeLKRepositoryService"
