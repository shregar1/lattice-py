
from repositories.atomic.candidate.candidate_location import CandidateLocationRepository

class TestCandidateLocationRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateLocationRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateLocationRepository"

