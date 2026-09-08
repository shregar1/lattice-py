
from orchestrator.api.v1.sourcing.validate_dedup_resolution import ValidateDedupResolutionService

class TestValidateDedupResolutionService:

    def test_service_instantiation(self) -> None:
        service = ValidateDedupResolutionService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestValidateDedupResolutionService"

