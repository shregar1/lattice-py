
from orchestrator.api.v1.sourcing.validate_sourced_profile import ValidateSourcedProfileService

class TestValidateSourcedProfileService:

    def test_service_instantiation(self) -> None:
        service = ValidateSourcedProfileService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestValidateSourcedProfileService"

