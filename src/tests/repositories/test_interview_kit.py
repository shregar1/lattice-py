
from repositories.interview.interview_kit import InterviewKitRepository

class TestInterviewKitRepository:

    def test_repository_instantiation(self) -> None:
        repo = InterviewKitRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestInterviewKitRepository"

