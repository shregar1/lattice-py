
import pytest
from dtos import SubmitCriteriaEvaluationRequest

class TestSubmitCriteriaEvaluationRequest:

    def test_schema_valid(self) -> None:
        schema = SubmitCriteriaEvaluationRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SubmitCriteriaEvaluationRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SubmitCriteriaEvaluationRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSubmitCriteriaEvaluationRequest"

