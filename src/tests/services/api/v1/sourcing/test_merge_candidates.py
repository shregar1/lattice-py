
from orchestrator.api.v1.sourcing.merge_candidates import MergeCandidatesService

class TestMergeCandidatesService:

    def test_service_instantiation(self) -> None:
        service = MergeCandidatesService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMergeCandidatesService"

