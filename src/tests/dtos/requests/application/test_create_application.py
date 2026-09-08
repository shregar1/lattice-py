
import pytest
from dtos import CreateApplicationRequest

class TestCreateApplicationRequest:

    def test_schema_valid(self) -> None:
        schema = CreateApplicationRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateApplicationRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateApplicationRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateApplicationRequest"

