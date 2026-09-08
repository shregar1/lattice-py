
import pytest
from dtos import CreateInterviewRequest

class TestCreateInterviewRequest:

    def test_schema_valid(self) -> None:
        schema = CreateInterviewRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateInterviewRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateInterviewRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateInterviewRequest"

