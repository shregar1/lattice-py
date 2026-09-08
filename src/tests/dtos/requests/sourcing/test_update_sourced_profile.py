
import pytest
from dtos import UpdateSourcedProfileRequest

class TestUpdateSourcedProfileRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateSourcedProfileRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateSourcedProfileRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateSourcedProfileRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateSourcedProfileRequest"

