
import pytest
from dtos import CreateAIScreeningConfigRequest

class TestCreateAIScreeningConfigRequest:

    def test_schema_valid(self) -> None:
        schema = CreateAIScreeningConfigRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateAIScreeningConfigRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateAIScreeningConfigRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAIScreeningConfigRequest"

