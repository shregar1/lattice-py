
import pytest
from dtos import ApplicationResponse

class TestApplicationResponse:

    def test_schema_valid(self) -> None:
        schema = ApplicationResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ApplicationResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ApplicationResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestApplicationResponse"

