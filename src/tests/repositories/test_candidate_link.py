
from repositories.atomic.candidate.candidate_link import CandidateLinkRepository

class TestCandidateLinkRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateLinkRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateLinkRepository"

