
from repositories.sourced_profile.sourced_profile_skill import SourcedProfileSkillRepository

class TestSourcedProfileSkillRepository:

    def test_repository_instantiation(self) -> None:
        repo = SourcedProfileSkillRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSourcedProfileSkillRepository"

