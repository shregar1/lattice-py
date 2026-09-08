
from repositories.interview.scheduling_link import SchedulingLinkRepository

class TestSchedulingLinkRepository:

    def test_repository_instantiation(self) -> None:
        repo = SchedulingLinkRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_slug_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'find_by_slug')
        assert callable(getattr(repo, 'find_by_slug'))

    def test_find_by_owner_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'find_by_owner')
        assert callable(getattr(repo, 'find_by_owner'))

    def test_find_active_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'find_active')
        assert callable(getattr(repo, 'find_active'))

    def test_find_by_job_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'find_by_job')
        assert callable(getattr(repo, 'find_by_job'))

    def test_find_by_duration_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'find_by_duration')
        assert callable(getattr(repo, 'find_by_duration'))

    def test_count_active_by_owner_callable(self) -> None:
        repo = SchedulingLinkRepository()
        assert hasattr(repo, 'count_active_by_owner')
        assert callable(getattr(repo, 'count_active_by_owner'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSchedulingLinkRepository"

