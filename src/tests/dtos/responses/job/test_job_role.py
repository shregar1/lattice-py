
import pytest
from dtos import JobRoleResponse

class TestJobRoleResponse:

    def test_schema_valid(self) -> None:
        schema = JobRoleResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = JobRoleResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                JobRoleResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobRoleResponse"

