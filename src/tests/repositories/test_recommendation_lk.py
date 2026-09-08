
from repositories.lookup.recommendation_lk import RecommendationLKRepository

class TestRecommendationLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = RecommendationLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRecommendationLKRepository"

