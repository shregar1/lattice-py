
from orchestrator.api.v1.automation.check_rule_triggers import CheckRuleTriggersService

class TestCheckRuleTriggersService:

    def test_service_instantiation(self) -> None:
        service = CheckRuleTriggersService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCheckRuleTriggersService"

