
import pytest
from dtos import AIScreeningConfigResponse

class TestAIScreeningConfigResponse:

    def test_schema_valid(self) -> None:
        schema = AIScreeningConfigResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AIScreeningConfigResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AIScreeningConfigResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningConfigResponse"

