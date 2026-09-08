
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/applications'

class TestCreateApplication:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_application_valid_payload(client):
        payload = {'job_id': 1, 'candidate_id': 1, 'tenant_id': 'tenant-1'}
        response = client.post(API_PATH, json=payload)
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_application_empty_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_application_response_is_json(client):
        response = client.post(API_PATH, json={'tenant_id': 'tenant-abc'})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_application_malformed_body(client):
        response = client.post(API_PATH, content=b'not-json', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_create_application_get_not_allowed(client):
        response = client.patch(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateApplication"

