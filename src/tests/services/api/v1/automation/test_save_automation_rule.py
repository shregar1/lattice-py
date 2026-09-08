
from orchestrator.api.v1.automation.save_automation_rule import SaveAutomationRuleService

class TestSaveAutomationRuleService:

    def test_service_instantiation(self) -> None:
        service = SaveAutomationRuleService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSaveAutomationRuleService"

