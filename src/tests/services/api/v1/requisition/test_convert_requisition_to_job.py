
from orchestrator.api.v1.requisition.convert_requisition_to_job import ConvertRequisitionToJobService

class TestConvertRequisitionToJobService:

    def test_service_instantiation(self) -> None:
        service = ConvertRequisitionToJobService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestConvertRequisitionToJobService"

