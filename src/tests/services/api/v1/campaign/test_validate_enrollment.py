
from orchestrator.api.v1.campaign.validate_enrollment import ValidateEnrollmentService

class TestValidateEnrollmentService:

    def test_service_instantiation(self) -> None:
        service = ValidateEnrollmentService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestValidateEnrollmentService"

