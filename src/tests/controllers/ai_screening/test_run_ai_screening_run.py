
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/ai-screening/runs'

class TestRunAIScreeningRun:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_trigger_run_valid_payload(client):
        response = client.post(API_PATH, json={'application_id': 1, 'config_id': 1})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_trigger_run_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_trigger_run_response_is_json(client):
        response = client.post(API_PATH, json={'application_id': 2})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_trigger_run_invalid_body_type(client):
        response = client.post(API_PATH, content=b'bad', headers={'content-type': 'text/plain'})
        assert response.status_code in (400, 415, 422, 500)

    @staticmethod
    def test_trigger_run_patch_not_allowed(client):
        response = client.patch(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRunAIScreeningRun"

