"""Base abstraction for country_lk repository service."""

from .abstraction import IAtomicRepositoryService


class ICountryLKRepositoryService(IAtomicRepositoryService):
    """Marker base for country_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICountryLKRepositoryService"
