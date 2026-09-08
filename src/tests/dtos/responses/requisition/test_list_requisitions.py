
import pytest
from dtos import ListRequisitionsResponse

class TestListRequisitionsResponse:

    def test_schema_valid(self) -> None:
        schema = ListRequisitionsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListRequisitionsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListRequisitionsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRequisitionsResponse"

