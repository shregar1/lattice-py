
import pytest
from dtos import CreateJobRequest

class TestCreateJobRequest:

    def test_schema_valid(self) -> None:
        schema = CreateJobRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateJobRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateJobRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateJobRequest"

