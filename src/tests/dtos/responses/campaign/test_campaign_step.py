
import pytest
from dtos import CampaignStepResponse

class TestCampaignStepResponse:

    def test_schema_valid(self) -> None:
        schema = CampaignStepResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CampaignStepResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CampaignStepResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCampaignStepResponse"

