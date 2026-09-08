
from orchestrator.api.v1.sourcing.add_to_pool import AddToPoolService

class TestAddToPoolService:

    def test_service_instantiation(self) -> None:
        service = AddToPoolService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAddToPoolService"

