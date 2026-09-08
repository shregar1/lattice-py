
import pytest
from dtos import ListTenantsRequest

class TestListTenantsRequest:

    def test_schema_valid(self) -> None:
        schema = ListTenantsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListTenantsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListTenantsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListTenantsRequest"

