
import pytest
from dtos import GetCandidateRequest

class TestGetCandidateRequest:

    def test_schema_valid(self) -> None:
        schema = GetCandidateRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = GetCandidateRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                GetCandidateRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetCandidateRequest"

