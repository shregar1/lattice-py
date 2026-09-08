"""Base abstraction for currency_lk repository service."""

from .abstraction import IAtomicRepositoryService


class ICurrencyLKRepositoryService(IAtomicRepositoryService):
    """Marker base for currency_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICurrencyLKRepositoryService"
