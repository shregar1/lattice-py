
from repositories.ai_screening.ai_screening_criteria import AIScreeningCriteriaRepository

class TestAIScreeningCriteriaRepository:

    def test_repository_instantiation(self) -> None:
        repo = AIScreeningCriteriaRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningCriteriaRepository"

