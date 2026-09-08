
import pytest
from dtos import CreateOfferRequest

class TestCreateOfferRequest:

    def test_schema_valid(self) -> None:
        schema = CreateOfferRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateOfferRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateOfferRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateOfferRequest"

