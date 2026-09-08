
from orchestrator.api.v1.tenant.create_tenant_orchestrator import CreateTenantOrchestratorService

class TestCreateTenantOrchestratorService:

    def test_service_instantiation(self) -> None:
        service = CreateTenantOrchestratorService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateTenantOrchestratorService"

