
import pytest
from dtos import CreateAIScreeningCriteriaRequest

class TestCreateAIScreeningCriteriaRequest:

    def test_schema_valid(self) -> None:
        schema = CreateAIScreeningCriteriaRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateAIScreeningCriteriaRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateAIScreeningCriteriaRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAIScreeningCriteriaRequest"

