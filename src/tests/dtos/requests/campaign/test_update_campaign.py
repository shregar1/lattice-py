
import pytest
from dtos import UpdateCampaignRequest

class TestUpdateCampaignRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateCampaignRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateCampaignRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateCampaignRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateCampaignRequest"

