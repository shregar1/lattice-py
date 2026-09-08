
from repositories.interview.scheduling_link_interviewer import SchedulingLinkInterviewerRepository

class TestSchedulingLinkInterviewerRepository:

    def test_repository_instantiation(self) -> None:
        repo = SchedulingLinkInterviewerRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSchedulingLinkInterviewerRepository"

