
import pytest
from dtos import ArchiveApplicationRequest

class TestArchiveApplicationRequest:

    def test_schema_valid(self) -> None:
        schema = ArchiveApplicationRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ArchiveApplicationRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ArchiveApplicationRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestArchiveApplicationRequest"

