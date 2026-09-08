
from repositories.enrollment import EnrollmentRepository

class TestEnrollmentRepository:

    def test_repository_instantiation(self) -> None:
        repo = EnrollmentRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_campaign_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'find_by_campaign')
        assert callable(getattr(repo, 'find_by_campaign'))

    def test_find_by_candidate_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'find_by_candidate')
        assert callable(getattr(repo, 'find_by_candidate'))

    def test_find_by_status_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'find_by_status')
        assert callable(getattr(repo, 'find_by_status'))

    def test_find_by_campaign_and_status_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'find_by_campaign_and_status')
        assert callable(getattr(repo, 'find_by_campaign_and_status'))

    def test_find_at_step_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'find_at_step')
        assert callable(getattr(repo, 'find_at_step'))

    def test_count_by_campaign_callable(self) -> None:
        repo = EnrollmentRepository()
        assert hasattr(repo, 'count_by_campaign')
        assert callable(getattr(repo, 'count_by_campaign'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEnrollmentRepository"

