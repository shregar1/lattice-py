
from repositories.tenant.tenant import TenantRepository

class TestTenantRepository:

    def test_repository_instantiation(self) -> None:
        repo = TenantRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_subdomain_callable(self) -> None:
        repo = TenantRepository()
        assert hasattr(repo, 'find_by_subdomain')
        assert callable(getattr(repo, 'find_by_subdomain'))

    def test_find_active_callable(self) -> None:
        repo = TenantRepository()
        assert hasattr(repo, 'find_active')
        assert callable(getattr(repo, 'find_active'))

    def test_find_inactive_callable(self) -> None:
        repo = TenantRepository()
        assert hasattr(repo, 'find_inactive')
        assert callable(getattr(repo, 'find_inactive'))

    def test_count_active_callable(self) -> None:
        repo = TenantRepository()
        assert hasattr(repo, 'count_active')
        assert callable(getattr(repo, 'count_active'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTenantRepository"

