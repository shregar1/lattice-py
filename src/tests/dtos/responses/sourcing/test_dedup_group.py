
import pytest
from dtos import DedupGroupResponse

class TestDedupGroupResponse:

    def test_schema_valid(self) -> None:
        schema = DedupGroupResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = DedupGroupResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                DedupGroupResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDedupGroupResponse"

