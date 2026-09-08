"""Base abstraction for location_lk repository service."""

from .abstraction import IAtomicRepositoryService


class ILocationLKRepositoryService(IAtomicRepositoryService):
    """Marker base for location_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ILocationLKRepositoryService"
