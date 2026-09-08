
from repositories.atomic.candidate.candidate_skill import CandidateSkillRepository

class TestCandidateSkillRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateSkillRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateSkillRepository"

