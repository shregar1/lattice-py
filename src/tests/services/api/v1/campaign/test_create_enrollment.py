
from orchestrator.api.v1.campaign.create_enrollment import CreateEnrollmentService

class TestCreateEnrollmentService:

    def test_service_instantiation(self) -> None:
        service = CreateEnrollmentService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateEnrollmentService"

