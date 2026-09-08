
from orchestrator.api.v1.application.create_initial_activity import CreateInitialActivityService

class TestCreateInitialActivityService:

    def test_service_instantiation(self) -> None:
        service = CreateInitialActivityService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateInitialActivityService"

