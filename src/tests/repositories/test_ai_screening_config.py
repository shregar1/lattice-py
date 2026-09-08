
from repositories.ai_screening.ai_screening_config import AIScreeningConfigRepository

class TestAIScreeningConfigRepository:

    def test_repository_instantiation(self) -> None:
        repo = AIScreeningConfigRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_job_callable(self) -> None:
        repo = AIScreeningConfigRepository()
        assert hasattr(repo, 'find_by_job')
        assert callable(getattr(repo, 'find_by_job'))

    def test_find_active_callable(self) -> None:
        repo = AIScreeningConfigRepository()
        assert hasattr(repo, 'find_active')
        assert callable(getattr(repo, 'find_active'))

    def test_find_active_by_job_callable(self) -> None:
        repo = AIScreeningConfigRepository()
        assert hasattr(repo, 'find_active_by_job')
        assert callable(getattr(repo, 'find_active_by_job'))

    def test_find_high_max_score_callable(self) -> None:
        repo = AIScreeningConfigRepository()
        assert hasattr(repo, 'find_high_max_score')
        assert callable(getattr(repo, 'find_high_max_score'))

    def test_count_active_callable(self) -> None:
        repo = AIScreeningConfigRepository()
        assert hasattr(repo, 'count_active')
        assert callable(getattr(repo, 'count_active'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningConfigRepository"

