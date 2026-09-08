
from orchestrator.api.v1.requisition.list_requisitions import ListRequisitionsService

class TestListRequisitionsService:

    def test_service_instantiation(self) -> None:
        service = ListRequisitionsService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRequisitionsService"

