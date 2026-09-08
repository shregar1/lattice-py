
from orchestrator.api.v1.tenant.notify_tenant_admin import NotifyTenantAdminService

class TestNotifyTenantAdminService:

    def test_service_instantiation(self) -> None:
        service = NotifyTenantAdminService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestNotifyTenantAdminService"

