
import pytest
from dtos import AddSchedulingLinkInterviewerRequest

class TestAddSchedulingLinkInterviewerRequest:

    def test_schema_valid(self) -> None:
        schema = AddSchedulingLinkInterviewerRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AddSchedulingLinkInterviewerRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AddSchedulingLinkInterviewerRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAddSchedulingLinkInterviewerRequest"

