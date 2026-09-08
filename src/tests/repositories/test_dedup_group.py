
from repositories.dedup.dedup_group import DedupGroupRepository

class TestDedupGroupRepository:

    def test_repository_instantiation(self) -> None:
        repo = DedupGroupRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_primary_candidate_callable(self) -> None:
        repo = DedupGroupRepository()
        assert hasattr(repo, 'find_by_primary_candidate')
        assert callable(getattr(repo, 'find_by_primary_candidate'))

    def test_find_unresolved_callable(self) -> None:
        repo = DedupGroupRepository()
        assert hasattr(repo, 'find_unresolved')
        assert callable(getattr(repo, 'find_unresolved'))

    def test_find_resolved_callable(self) -> None:
        repo = DedupGroupRepository()
        assert hasattr(repo, 'find_resolved')
        assert callable(getattr(repo, 'find_resolved'))

    def test_find_resolved_after_callable(self) -> None:
        repo = DedupGroupRepository()
        assert hasattr(repo, 'find_resolved_after')
        assert callable(getattr(repo, 'find_resolved_after'))

    def test_count_unresolved_callable(self) -> None:
        repo = DedupGroupRepository()
        assert hasattr(repo, 'count_unresolved')
        assert callable(getattr(repo, 'count_unresolved'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDedupGroupRepository"

