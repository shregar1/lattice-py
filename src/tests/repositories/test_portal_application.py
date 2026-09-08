
from repositories.application.portal_application import PortalApplicationRepository

class TestPortalApplicationRepository:

    def test_repository_instantiation(self) -> None:
        repo = PortalApplicationRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_code_callable(self) -> None:
        repo = PortalApplicationRepository()
        assert hasattr(repo, 'find_by_code')
        assert callable(getattr(repo, 'find_by_code'))

    def test_find_by_candidate_callable(self) -> None:
        repo = PortalApplicationRepository()
        assert hasattr(repo, 'find_by_candidate')
        assert callable(getattr(repo, 'find_by_candidate'))

    def test_find_by_job_callable(self) -> None:
        repo = PortalApplicationRepository()
        assert hasattr(repo, 'find_by_job')
        assert callable(getattr(repo, 'find_by_job'))

    def test_find_by_candidate_and_job_callable(self) -> None:
        repo = PortalApplicationRepository()
        assert hasattr(repo, 'find_by_candidate_and_job')
        assert callable(getattr(repo, 'find_by_candidate_and_job'))

    def test_count_by_job_callable(self) -> None:
        repo = PortalApplicationRepository()
        assert hasattr(repo, 'count_by_job')
        assert callable(getattr(repo, 'count_by_job'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestPortalApplicationRepository"

