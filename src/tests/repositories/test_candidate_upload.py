
from repositories.atomic.candidate.candidate_upload import CandidateUploadRepository

class TestCandidateUploadRepository:

    def test_repository_instantiation(self) -> None:
        repo = CandidateUploadRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateUploadRepository"

