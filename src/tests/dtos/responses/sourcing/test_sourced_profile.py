
import pytest
from dtos import SourcedProfileResponse

class TestSourcedProfileResponse:

    def test_schema_valid(self) -> None:
        schema = SourcedProfileResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SourcedProfileResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SourcedProfileResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSourcedProfileResponse"

