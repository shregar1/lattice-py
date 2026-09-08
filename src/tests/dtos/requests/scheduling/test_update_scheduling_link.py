
import pytest
from dtos import UpdateSchedulingLinkRequest

class TestUpdateSchedulingLinkRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateSchedulingLinkRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateSchedulingLinkRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateSchedulingLinkRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateSchedulingLinkRequest"

