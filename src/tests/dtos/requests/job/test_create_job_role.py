
import pytest
from dtos import CreateJobRoleRequest

class TestCreateJobRoleRequest:

    def test_schema_valid(self) -> None:
        schema = CreateJobRoleRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateJobRoleRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateJobRoleRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateJobRoleRequest"

