
import pytest
from dtos import MoveApplicationStageRequest

class TestMoveApplicationStageRequest:

    def test_schema_valid(self) -> None:
        schema = MoveApplicationStageRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = MoveApplicationStageRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                MoveApplicationStageRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMoveApplicationStageRequest"

