
import pytest
from dtos import UpdateApplicationRatingRequest

class TestUpdateApplicationRatingRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateApplicationRatingRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateApplicationRatingRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateApplicationRatingRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateApplicationRatingRequest"

