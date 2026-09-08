
import pytest
from dtos import ListCampaignsResponse

class TestListCampaignsResponse:

    def test_schema_valid(self) -> None:
        schema = ListCampaignsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListCampaignsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListCampaignsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListCampaignsResponse"

