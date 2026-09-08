
from repositories.job.job_interview_plan import JobInterviewPlanRepository

class TestJobInterviewPlanRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobInterviewPlanRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobInterviewPlanRepository"

