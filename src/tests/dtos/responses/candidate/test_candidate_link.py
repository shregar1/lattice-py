
import pytest
from dtos import CandidateLinkResponse

class TestCandidateLinkResponse:

    def test_schema_valid(self) -> None:
        schema = CandidateLinkResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CandidateLinkResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CandidateLinkResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCandidateLinkResponse"

