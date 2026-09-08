
from repositories.rule.automation_rule import AutomationRuleRepository

class TestAutomationRuleRepository:

    def test_repository_instantiation(self) -> None:
        repo = AutomationRuleRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_active_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_active')
        assert callable(getattr(repo, 'find_active'))

    def test_find_by_trigger_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_by_trigger')
        assert callable(getattr(repo, 'find_by_trigger'))

    def test_find_by_action_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_by_action')
        assert callable(getattr(repo, 'find_by_action'))

    def test_find_by_trigger_stage_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_by_trigger_stage')
        assert callable(getattr(repo, 'find_by_trigger_stage'))

    def test_find_by_action_stage_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_by_action_stage')
        assert callable(getattr(repo, 'find_by_action_stage'))

    def test_find_by_action_tag_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_by_action_tag')
        assert callable(getattr(repo, 'find_by_action_tag'))

    def test_find_high_run_count_callable(self) -> None:
        repo = AutomationRuleRepository()
        assert hasattr(repo, 'find_high_run_count')
        assert callable(getattr(repo, 'find_high_run_count'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAutomationRuleRepository"

