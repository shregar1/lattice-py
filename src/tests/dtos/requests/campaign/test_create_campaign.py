
import pytest
from dtos import CreateCampaignRequest

class TestCreateCampaignRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCampaignRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCampaignRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCampaignRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCampaignRequest"

