
from repositories.notification import NotificationRepository

class TestNotificationRepository:

    def test_repository_instantiation(self) -> None:
        repo = NotificationRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_user_account_callable(self) -> None:
        repo = NotificationRepository()
        assert hasattr(repo, 'find_by_user_account')
        assert callable(getattr(repo, 'find_by_user_account'))

    def test_find_unread_callable(self) -> None:
        repo = NotificationRepository()
        assert hasattr(repo, 'find_unread')
        assert callable(getattr(repo, 'find_unread'))

    def test_find_by_kind_callable(self) -> None:
        repo = NotificationRepository()
        assert hasattr(repo, 'find_by_kind')
        assert callable(getattr(repo, 'find_by_kind'))

    def test_count_unread_callable(self) -> None:
        repo = NotificationRepository()
        assert hasattr(repo, 'count_unread')
        assert callable(getattr(repo, 'count_unread'))

    def test_find_read_callable(self) -> None:
        repo = NotificationRepository()
        assert hasattr(repo, 'find_read')
        assert callable(getattr(repo, 'find_read'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestNotificationRepository"

