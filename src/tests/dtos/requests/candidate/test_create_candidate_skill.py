
import pytest
from dtos import CreateCandidateSkillRequest

class TestCreateCandidateSkillRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCandidateSkillRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCandidateSkillRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCandidateSkillRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCandidateSkillRequest"

