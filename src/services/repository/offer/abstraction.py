"""Base abstraction for offer repository service."""

from .abstraction import IAtomicRepositoryService


class IOfferRepositoryService(IAtomicRepositoryService):
    """Marker base for offer repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IOfferRepositoryService"
