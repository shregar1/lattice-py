"""Base abstraction for campaign repository service."""

from .abstraction import IAtomicRepositoryService


class ICampaignRepositoryService(IAtomicRepositoryService):
    """Marker base for campaign repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICampaignRepositoryService"
