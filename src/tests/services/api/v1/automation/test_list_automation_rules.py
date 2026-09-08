
from orchestrator.api.v1.automation.list_automation_rules import ListAutomationRulesService

class TestListAutomationRulesService:

    def test_service_instantiation(self) -> None:
        service = ListAutomationRulesService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListAutomationRulesService"

