
from repositories.lookup.template_type_lk import TemplateTypeLKRepository

class TestTemplateTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = TemplateTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTemplateTypeLKRepository"

