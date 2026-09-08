
from orchestrator.api.v1.ai_screening.extract_candidate_data import ExtractCandidateDataService

class TestExtractCandidateDataService:

    def test_service_instantiation(self) -> None:
        service = ExtractCandidateDataService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestExtractCandidateDataService"

