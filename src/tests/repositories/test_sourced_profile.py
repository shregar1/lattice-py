
from repositories.sourced_profile.sourced_profile import SourcedProfileRepository

class TestSourcedProfileRepository:

    def test_repository_instantiation(self) -> None:
        repo = SourcedProfileRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_added_to_pool_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'find_added_to_pool')
        assert callable(getattr(repo, 'find_added_to_pool'))

    def test_find_by_location_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'find_by_location')
        assert callable(getattr(repo, 'find_by_location'))

    def test_find_high_match_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'find_high_match')
        assert callable(getattr(repo, 'find_high_match'))

    def test_search_by_name_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'search_by_name')
        assert callable(getattr(repo, 'search_by_name'))

    def test_search_by_headline_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'search_by_headline')
        assert callable(getattr(repo, 'search_by_headline'))

    def test_count_added_to_pool_callable(self) -> None:
        repo = SourcedProfileRepository()
        assert hasattr(repo, 'count_added_to_pool')
        assert callable(getattr(repo, 'count_added_to_pool'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSourcedProfileRepository"

