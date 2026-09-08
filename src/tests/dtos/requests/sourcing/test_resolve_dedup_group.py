
import pytest
from dtos import ResolveDedupGroupRequest

class TestResolveDedupGroupRequest:

    def test_schema_valid(self) -> None:
        schema = ResolveDedupGroupRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ResolveDedupGroupRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ResolveDedupGroupRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestResolveDedupGroupRequest"

