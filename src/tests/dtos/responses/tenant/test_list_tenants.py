
import pytest
from dtos import ListTenantsResponse

class TestListTenantsResponse:

    def test_schema_valid(self) -> None:
        schema = ListTenantsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListTenantsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListTenantsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListTenantsResponse"

