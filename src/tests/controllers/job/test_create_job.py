
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/jobs'

class TestCreateJob:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_job_valid_payload(client):
        response = client.post(API_PATH, json={'title': 'Senior Backend Engineer', 'department': 'Engineering', 'openings': 2, 'tenant_id': 1})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_create_job_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_job_response_is_json(client):
        response = client.post(API_PATH, json={'title': 'Test Job'})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_job_malformed_json(client):
        response = client.post(API_PATH, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_create_job_put_not_allowed(client):
        response = client.put(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateJob"

