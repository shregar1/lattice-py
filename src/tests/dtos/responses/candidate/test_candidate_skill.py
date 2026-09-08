
import pytest
from dtos import CandidateSkillResponse

class TestCandidateSkillResponse:

    def test_schema_valid(self) -> None:
        schema = CandidateSkillResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CandidateSkillResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CandidateSkillResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateSkillResponse"

