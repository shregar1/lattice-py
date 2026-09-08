
import pytest
from dtos import ListRequisitionsRequest

class TestListRequisitionsRequest:

    def test_schema_valid(self) -> None:
        schema = ListRequisitionsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListRequisitionsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListRequisitionsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRequisitionsRequest"

