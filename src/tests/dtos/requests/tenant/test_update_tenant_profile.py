
import pytest
from dtos import UpdateTenantProfileRequest

class TestUpdateTenantProfileRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateTenantProfileRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateTenantProfileRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateTenantProfileRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateTenantProfileRequest"

