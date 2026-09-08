
import pytest
from dtos import CandidateTagResponse

class TestCandidateTagResponse:

    def test_schema_valid(self) -> None:
        schema = CandidateTagResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CandidateTagResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CandidateTagResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateTagResponse"

