
from orchestrator.api.v1.automation.create_automation_rule_orchestrator import CreateAutomationRuleOrchestratorService

class TestCreateAutomationRuleOrchestratorService:

    def test_service_instantiation(self) -> None:
        service = CreateAutomationRuleOrchestratorService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAutomationRuleOrchestratorService"

