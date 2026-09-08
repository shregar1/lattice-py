
import pytest
from dtos import CreateCandidateRequest

class TestCreateCandidateRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCandidateRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCandidateRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCandidateRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCandidateRequest"

