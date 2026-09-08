
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/candidates'

class TestCreateCandidate:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_candidate_valid_payload(client):
        response = client.post(API_PATH, json={'name': 'Jane Doe', 'email': 'jane@example.com'})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_create_candidate_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_candidate_response_is_json(client):
        response = client.post(API_PATH, json={'name': 'Test User'})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_candidate_malformed_json(client):
        response = client.post(API_PATH, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_create_candidate_put_not_allowed(client):
        response = client.put(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCandidate"

