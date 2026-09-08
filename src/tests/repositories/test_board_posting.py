
from repositories.board_posting import BoardPostingRepository

class TestBoardPostingRepository:

    def test_repository_instantiation(self) -> None:
        repo = BoardPostingRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_job_callable(self) -> None:
        repo = BoardPostingRepository()
        assert hasattr(repo, 'find_by_job')
        assert callable(getattr(repo, 'find_by_job'))

    def test_find_active_by_job_callable(self) -> None:
        repo = BoardPostingRepository()
        assert hasattr(repo, 'find_active_by_job')
        assert callable(getattr(repo, 'find_active_by_job'))

    def test_find_by_board_callable(self) -> None:
        repo = BoardPostingRepository()
        assert hasattr(repo, 'find_by_board')
        assert callable(getattr(repo, 'find_by_board'))

    def test_find_active_by_board_callable(self) -> None:
        repo = BoardPostingRepository()
        assert hasattr(repo, 'find_active_by_board')
        assert callable(getattr(repo, 'find_active_by_board'))

    def test_count_active_by_job_callable(self) -> None:
        repo = BoardPostingRepository()
        assert hasattr(repo, 'count_active_by_job')
        assert callable(getattr(repo, 'count_active_by_job'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestBoardPostingRepository"

