
from repositories.tenant.tenant_profile import TenantProfileRepository

class TestTenantProfileRepository:

    def test_repository_instantiation(self) -> None:
        repo = TenantProfileRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTenantProfileRepository"

