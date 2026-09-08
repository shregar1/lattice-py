
from orchestrator.api.v1.automation.list_rule_runs import ListRuleRunsService

class TestListRuleRunsService:

    def test_service_instantiation(self) -> None:
        service = ListRuleRunsService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRuleRunsService"

