
import pytest
from dtos import EnrollCandidateRequest

class TestEnrollCandidateRequest:

    def test_schema_valid(self) -> None:
        schema = EnrollCandidateRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = EnrollCandidateRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                EnrollCandidateRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEnrollCandidateRequest"

