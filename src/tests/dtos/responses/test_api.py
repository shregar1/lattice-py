
from dtos import IResponseDTO
from enums.api_response_status import ApiResponseStatus

class TestIResponseDTO:

    def test_success_envelope_creation(self) -> None:
        env = IResponseDTO.success(data={'foo': 'bar'}, response_message='Success', response_key='OK')
        assert env.status == ApiResponseStatus.SUCCESS
        assert env.response_message == 'Success'
        assert env.response_key == 'OK'
        assert env.data == {'foo': 'bar'}
        assert env.transaction_urn is not None

    def test_failed_envelope_creation(self) -> None:
        env = IResponseDTO.failed(response_message='Failed to process', response_key='ERROR_KEY')
        assert env.status == ApiResponseStatus.FAILED
        assert env.response_message == 'Failed to process'
        assert env.response_key == 'ERROR_KEY'
        assert len(env.errors) == 1

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestIResponseDTO"

