
import pytest
from dtos import TenantProfileResponse

class TestTenantProfileResponse:

    def test_schema_valid(self) -> None:
        schema = TenantProfileResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = TenantProfileResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                TenantProfileResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTenantProfileResponse"

