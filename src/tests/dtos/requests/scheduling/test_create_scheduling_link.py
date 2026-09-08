
import pytest
from dtos import CreateSchedulingLinkRequest

class TestCreateSchedulingLinkRequest:

    def test_schema_valid(self) -> None:
        schema = CreateSchedulingLinkRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateSchedulingLinkRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateSchedulingLinkRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateSchedulingLinkRequest"

