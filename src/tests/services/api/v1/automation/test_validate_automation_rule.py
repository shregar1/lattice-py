
from orchestrator.api.v1.automation.validate_automation_rule import ValidateAutomationRuleService

class TestValidateAutomationRuleService:

    def test_service_instantiation(self) -> None:
        service = ValidateAutomationRuleService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestValidateAutomationRuleService"

