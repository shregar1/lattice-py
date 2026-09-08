
from repositories.user.user import UserRepository

class TestUserRepository:

    def test_repository_instantiation(self) -> None:
        repo = UserRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_tenant_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_tenant')
        assert callable(getattr(repo, 'find_by_tenant'))

    def test_find_by_account_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_account')
        assert callable(getattr(repo, 'find_by_account'))

    def test_find_by_type_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_type')
        assert callable(getattr(repo, 'find_by_type'))

    def test_find_by_type_and_tenant_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_type_and_tenant')
        assert callable(getattr(repo, 'find_by_type_and_tenant'))

    def test_search_by_name_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'search_by_name')
        assert callable(getattr(repo, 'search_by_name'))

    def test_count_by_tenant_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'count_by_tenant')
        assert callable(getattr(repo, 'count_by_tenant'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUserRepository"

