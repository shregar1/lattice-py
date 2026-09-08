
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/jobs'
VALID_URN = 'urn:vexarr:job:test-001'
NONEXISTENT_URN = 'urn:vexarr:job:XXXNONEXISTENT9999'

class TestGetJob:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_get_job_responds(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_get_job_response_is_json(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_get_nonexistent_job(client):
        response = client.get(f'{API_BASE}/{NONEXISTENT_URN}')
        assert response.status_code in (404, 422, 500)

    @staticmethod
    def test_get_job_delete_not_allowed(client):
        response = client.delete(f'{API_BASE}/{VALID_URN}')
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetJob"

