
from repositories.atomic.candidate.candidate import CandidateRepository

class TestCandidateRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_email_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'find_by_email')
        assert callable(getattr(repo, 'find_by_email'))

    def test_find_by_tenant_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'find_by_tenant')
        assert callable(getattr(repo, 'find_by_tenant'))

    def test_find_by_account_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'find_by_account')
        assert callable(getattr(repo, 'find_by_account'))

    def test_search_by_name_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'search_by_name')
        assert callable(getattr(repo, 'search_by_name'))

    def test_count_by_tenant_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'count_by_tenant')
        assert callable(getattr(repo, 'count_by_tenant'))

    def test_find_deleted_callable(self) -> None:
        repo = CandidateRepository()
        assert hasattr(repo, 'find_deleted')
        assert callable(getattr(repo, 'find_deleted'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateRepository"

