
from repositories.interview.interview_interviewer import InterviewInterviewerRepository

class TestInterviewInterviewerRepository:

    def test_repository_instantiation(self) -> None:
        repo = InterviewInterviewerRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestInterviewInterviewerRepository"

