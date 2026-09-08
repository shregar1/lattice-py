
import pytest
from dtos import CampaignResponse

class TestCampaignResponse:

    def test_schema_valid(self) -> None:
        schema = CampaignResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CampaignResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CampaignResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCampaignResponse"

