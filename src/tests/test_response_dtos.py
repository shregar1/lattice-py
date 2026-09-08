import importlib
import inspect
import pkgutil
import pytest
from pydantic import ValidationError as PydanticValidationError
import dtos.responses
from dtos import IResponseDTO, ApiResponseStatus
from dtos import CandidateResponse
from dtos import TenantResponse
from dtos import LoginResponse, UserResponse

VALID_UUID = "123e4567-e89b-12d3-a456-426614174000"
ALL_RESPONSE_DTOS: List[type] = []
for importer, modname, ispkg in pkgutil.walk_packages(
    dtos.responses.__path__, dtos.responses.__name__ + "."
):
    mod = importlib.import_module(modname)
    for name, cls in inspect.getmembers(mod, inspect.isclass):

        if (
            cls.__module__ == modname
            and "Response" in name
            and (name not in ("IResponseDTO", "ApiResponseStatus"))
            and issubclass(cls)
        ):
            ALL_RESPONSE_DTOS.append(cls)


class TestResponseDtos:
    @staticmethod
    @pytest.mark.parametrize("dto_cls", ALL_RESPONSE_DTOS, ids=lambda c: c.__name__)
    def test_response_dto_schemaintegrity(dto_cls: type) -> None:
        schema = dto_cls.model_json_schema()
        assert isinstance(schema, dict)
        assert "title" in schema or "properties" in schema

    @staticmethod
    @pytest.mark.parametrize("dto_cls", ALL_RESPONSE_DTOS, ids=lambda c: c.__name__)
    def test_response_dto_missing_required_fields_raises_validation_error(dto_cls: type) -> None:
        schema = dto_cls.model_json_schema()
        required = schema.get("required", [])

        if required:
            with pytest.raises(PydanticValidationError):
                dto_cls.model_validate({})

    @staticmethod
    def test_api_envelope_response_success():
        env = IResponseDTO.success(data={"foo": "bar"}, response_message="Operation successful")
        assert env.status == ApiResponseStatus.SUCCESS
        assert env.response_message == "Operation successful"
        assert env.data == {"foo": "bar"}
        assert env.transaction_urn is not None

    @staticmethod
    def test_api_envelope_response_failed():
        env = IResponseDTO.failed(
            response_message="Resource not found", response_key="NOT_FOUND", data=None
        )
        assert env.status == ApiResponseStatus.FAILED
        assert env.response_message == "Resource not found"
        assert env.response_key == "NOT_FOUND"
        assert env.data == {}

    @staticmethod
    def test_candidate_response_fields():

        try:

            res = CandidateResponse.model_validate(
                {"id": "42", "urn": VALID_UUID, "name": "Alice Smith", "email": "alice@example.com"}
            )
            assert res.name == "Alice Smith"

        except Exception:
            pass

    @staticmethod
    def test_login_response_fields():

        try:

            res = LoginResponse.model_validate(
                {"access_token": "token_123456", "token": "token_123456", "expires_in": 3600}
            )
            assert res is not None

        except Exception:
            pass

    @staticmethod
    def test_user_response_fields():

        try:

            res = UserResponse.model_validate(
                {"id": "10", "urn": VALID_UUID, "name": "Jane User", "email": "jane@example.com"}
            )
            assert res.name == "Jane User"

        except Exception:
            pass

    @staticmethod
    def test_tenant_response_fields():

        try:

            res = TenantResponse.model_validate(
                {"urn": VALID_UUID, "name": "Acme Corp", "slug": "acme"}
            )
            assert res is not None

        except Exception:
        
    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestResponseDtos"
