
import pytest
from dtos import TenantResponse

class TestTenantResponse:

    def test_schema_valid(self) -> None:
        schema = TenantResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = TenantResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                TenantResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTenantResponse"

