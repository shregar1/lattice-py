
import pytest
from dtos import UpdateCandidateRequest

class TestUpdateCandidateRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateCandidateRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateCandidateRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateCandidateRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateCandidateRequest"

