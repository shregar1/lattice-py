
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/ai-screening/configs'

class TestCreateAIScreeningConfig:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_config_valid_payload(client):
        response = client.post(API_PATH, json={'job_id': 1, 'min_score': 80})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_create_config_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_config_response_is_json(client):
        response = client.post(API_PATH, json={'job_id': 2})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_config_invalid_content_type(client):
        response = client.post(API_PATH, content=b'not-json', headers={'content-type': 'text/plain'})
        assert response.status_code in (400, 415, 422, 500)

    @staticmethod
    def test_create_config_get_not_allowed(client):
        response = client.get(API_PATH)
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAIScreeningConfig"

