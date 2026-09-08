
import pytest
from dtos import CreateCandidateTagRequest

class TestCreateCandidateTagRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCandidateTagRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCandidateTagRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCandidateTagRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCandidateTagRequest"

