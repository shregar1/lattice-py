
import pytest
from dtos import ListSourcedProfilesResponse

class TestListSourcedProfilesResponse:

    def test_schema_valid(self) -> None:
        schema = ListSourcedProfilesResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSourcedProfilesResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSourcedProfilesResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSourcedProfilesResponse"

