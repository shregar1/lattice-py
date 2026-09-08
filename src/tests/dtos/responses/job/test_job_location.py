
import pytest
from dtos import JobLocationResponse

class TestJobLocationResponse:

    def test_schema_valid(self) -> None:
        schema = JobLocationResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = JobLocationResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                JobLocationResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobLocationResponse"

