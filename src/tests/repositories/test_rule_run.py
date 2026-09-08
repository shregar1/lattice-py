
from repositories.rule.rule_run import RuleRunRepository

class TestRuleRunRepository:

    def test_repository_instantiation(self) -> None:
        repo = RuleRunRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_rule_callable(self) -> None:
        repo = RuleRunRepository()
        assert hasattr(repo, 'find_by_rule')
        assert callable(getattr(repo, 'find_by_rule'))

    def test_find_by_candidate_callable(self) -> None:
        repo = RuleRunRepository()
        assert hasattr(repo, 'find_by_candidate')
        assert callable(getattr(repo, 'find_by_candidate'))

    def test_find_by_rule_and_candidate_callable(self) -> None:
        repo = RuleRunRepository()
        assert hasattr(repo, 'find_by_rule_and_candidate')
        assert callable(getattr(repo, 'find_by_rule_and_candidate'))

    def test_find_recent_callable(self) -> None:
        repo = RuleRunRepository()
        assert hasattr(repo, 'find_recent')
        assert callable(getattr(repo, 'find_recent'))

    def test_count_by_rule_callable(self) -> None:
        repo = RuleRunRepository()
        assert hasattr(repo, 'count_by_rule')
        assert callable(getattr(repo, 'count_by_rule'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRuleRunRepository"

