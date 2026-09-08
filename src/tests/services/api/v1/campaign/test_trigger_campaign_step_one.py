
from orchestrator.api.v1.campaign.trigger_campaign_step_one import TriggerCampaignStepOneService

class TestTriggerCampaignStepOneService:

    def test_service_instantiation(self) -> None:
        service = TriggerCampaignStepOneService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTriggerCampaignStepOneService"

