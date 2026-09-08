
import pytest
from dtos import GetApplicationRequest

class TestGetApplicationRequest:

    def test_schema_valid(self) -> None:
        schema = GetApplicationRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = GetApplicationRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                GetApplicationRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetApplicationRequest"

