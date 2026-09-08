
from repositories.lookup.ai_screening_status_lk import AIScreeningStatusLKRepository

class TestAIScreeningStatusLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = AIScreeningStatusLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningStatusLKRepository"

