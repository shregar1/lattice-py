
from repositories.lookup.upload_type_lk import UploadTypeLKRepository

class TestUploadTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = UploadTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUploadTypeLKRepository"

