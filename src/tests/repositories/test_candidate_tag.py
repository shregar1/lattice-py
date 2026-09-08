
from repositories.atomic.candidate.candidate_tag import CandidateTagRepository

class TestCandidateTagRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateTagRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateTagRepository"

