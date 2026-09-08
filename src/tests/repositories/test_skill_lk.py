
from repositories.lookup.skill_lk import SkillLKRepository

class TestSkillLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = SkillLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSkillLKRepository"

