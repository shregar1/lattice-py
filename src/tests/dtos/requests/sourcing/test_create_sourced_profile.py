
import pytest
from dtos import CreateSourcedProfileRequest

class TestCreateSourcedProfileRequest:

    def test_schema_valid(self) -> None:
        schema = CreateSourcedProfileRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateSourcedProfileRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateSourcedProfileRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateSourcedProfileRequest"

