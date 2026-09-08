
from orchestrator.api.v1.ai_screening.evaluate_ai_criteria import EvaluateAiCriteriaService

class TestEvaluateAiCriteriaService:

    def test_service_instantiation(self) -> None:
        service = EvaluateAiCriteriaService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEvaluateAiCriteriaService"

