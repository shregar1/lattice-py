"""Base abstraction for campaign_step repository service."""

from .abstraction import IAtomicRepositoryService


class ICampaignStepRepositoryService(IAtomicRepositoryService):
    """Marker base for campaign_step repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICampaignStepRepositoryService"
