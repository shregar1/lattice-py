
import pytest
from dtos import ListSourcedProfilesRequest

class TestListSourcedProfilesRequest:

    def test_schema_valid(self) -> None:
        schema = ListSourcedProfilesRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSourcedProfilesRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSourcedProfilesRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSourcedProfilesRequest"

