
from repositories.user_account import UserRepository

class TestUserRepository:

    def test_repository_instantiation(self) -> None:
        repo = UserRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_email_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_email')
        assert callable(getattr(repo, 'find_by_email'))

    def test_find_mfa_enabled_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_mfa_enabled')
        assert callable(getattr(repo, 'find_mfa_enabled'))

    def test_find_by_auth_type_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_auth_type')
        assert callable(getattr(repo, 'find_by_auth_type'))

    def test_find_by_mfa_type_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_by_mfa_type')
        assert callable(getattr(repo, 'find_by_mfa_type'))

    def test_find_recently_logged_in_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'find_recently_logged_in')
        assert callable(getattr(repo, 'find_recently_logged_in'))

    def test_count_mfa_enabled_callable(self) -> None:
        repo = UserRepository()
        assert hasattr(repo, 'count_mfa_enabled')
        assert callable(getattr(repo, 'count_mfa_enabled'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUserRepository"

