
from repositories.lookup.employment_type_lk import EmploymentTypeLKRepository

class TestEmploymentTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = EmploymentTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEmploymentTypeLKRepository"

