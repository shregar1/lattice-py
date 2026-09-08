
import pytest
from dtos import AddInterviewerRequest

class TestAddInterviewerRequest:

    def test_schema_valid(self) -> None:
        schema = AddInterviewerRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AddInterviewerRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AddInterviewerRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAddInterviewerRequest"

