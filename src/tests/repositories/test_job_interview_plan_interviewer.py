
from repositories.job.job_interview_plan_interviewer import JobInterviewPlanInterviewerRepository

class TestJobInterviewPlanInterviewerRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobInterviewPlanInterviewerRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobInterviewPlanInterviewerRepository"

