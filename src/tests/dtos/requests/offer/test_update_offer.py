
import pytest
from dtos import UpdateOfferRequest

class TestUpdateOfferRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateOfferRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateOfferRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateOfferRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateOfferRequest"

