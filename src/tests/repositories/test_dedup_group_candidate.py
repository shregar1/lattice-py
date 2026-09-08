
from repositories.dedup.dedup_group_candidate import DedupGroupCandidateRepository

class TestDedupGroupCandidateRepository:

    def test_repository_instantiation(self) -> None:
        repo = DedupGroupCandidateRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDedupGroupCandidateRepository"

