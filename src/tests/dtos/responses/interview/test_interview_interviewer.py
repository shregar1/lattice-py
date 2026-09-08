
import pytest
from dtos import InterviewInterviewerResponse

class TestInterviewInterviewerResponse:

    def test_schema_valid(self) -> None:
        schema = InterviewInterviewerResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = InterviewInterviewerResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                InterviewInterviewerResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestInterviewInterviewerResponse"

