
import pytest
from dtos import CreateJobLocationRequest

class TestCreateJobLocationRequest:

    def test_schema_valid(self) -> None:
        schema = CreateJobLocationRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateJobLocationRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateJobLocationRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateJobLocationRequest"

