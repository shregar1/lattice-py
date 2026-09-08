
import pytest
from dtos import JobResponse

class TestJobResponse:

    def test_schema_valid(self) -> None:
        schema = JobResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = JobResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                JobResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobResponse"

