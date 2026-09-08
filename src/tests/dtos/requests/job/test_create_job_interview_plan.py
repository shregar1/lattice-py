
import pytest
from dtos import CreateJobInterviewPlanRequest

class TestCreateJobInterviewPlanRequest:

    def test_schema_valid(self) -> None:
        schema = CreateJobInterviewPlanRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateJobInterviewPlanRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateJobInterviewPlanRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateJobInterviewPlanRequest"

