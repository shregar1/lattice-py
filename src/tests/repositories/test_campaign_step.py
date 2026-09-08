
from repositories.campaign.campaign_step import CampaignStepRepository

class TestCampaignStepRepository:

    def test_repository_instantiation(self) -> None:
        repo = CampaignStepRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCampaignStepRepository"

