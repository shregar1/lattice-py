
from repositories.ai_screening.ai_screening_evaluation import AIScreeningEvaluationRepository

class TestAIScreeningEvaluationRepository:

    def test_repository_instantiation(self) -> None:
        repo = AIScreeningEvaluationRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningEvaluationRepository"

