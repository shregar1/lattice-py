"""Base abstraction for rating_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IRatingLKRepositoryService(IAtomicRepositoryService):
    """Marker base for rating_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRatingLKRepositoryService"
