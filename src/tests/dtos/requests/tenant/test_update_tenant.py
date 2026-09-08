
import pytest
from dtos import UpdateTenantRequest

class TestUpdateTenantRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateTenantRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateTenantRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateTenantRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateTenantRequest"

