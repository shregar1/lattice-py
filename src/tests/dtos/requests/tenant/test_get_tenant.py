
import pytest
from dtos import GetTenantRequest

class TestGetTenantRequest:

    def test_schema_valid(self) -> None:
        schema = GetTenantRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = GetTenantRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                GetTenantRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetTenantRequest"

