
from orchestrator.api.v1.interview.cancel_interview import CancelInterviewService

class TestCancelInterviewService:

    def test_service_instantiation(self) -> None:
        service = CancelInterviewService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCancelInterviewService"

