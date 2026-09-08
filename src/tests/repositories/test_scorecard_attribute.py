
from repositories.scorecard.scorecard_attribute import ScorecardAttributeRepository

class TestScorecardAttributeRepository:

    def test_repository_instantiation(self) -> None:
        repo = ScorecardAttributeRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestScorecardAttributeRepository"

