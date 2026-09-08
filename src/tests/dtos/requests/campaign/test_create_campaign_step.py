
import pytest
from dtos import CreateCampaignStepRequest

class TestCreateCampaignStepRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCampaignStepRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCampaignStepRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCampaignStepRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCampaignStepRequest"

