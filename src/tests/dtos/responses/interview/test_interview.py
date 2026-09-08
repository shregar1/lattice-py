
import pytest
from dtos import InterviewResponse

class TestInterviewResponse:

    def test_schema_valid(self) -> None:
        schema = InterviewResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = InterviewResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                InterviewResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestInterviewResponse"

