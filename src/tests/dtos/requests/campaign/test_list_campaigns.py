
import pytest
from dtos import ListCampaignsRequest

class TestListCampaignsRequest:

    def test_schema_valid(self) -> None:
        schema = ListCampaignsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListCampaignsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListCampaignsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListCampaignsRequest"

