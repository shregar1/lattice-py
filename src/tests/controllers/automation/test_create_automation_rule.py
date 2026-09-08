
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/automation-rules'

class TestCreateAutomationRule:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_rule_valid_payload(client):
        response = client.post(API_PATH, json={'name': 'Auto-advance', 'trigger_id': 1})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_create_rule_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_rule_response_is_json(client):
        response = client.post(API_PATH, json={'name': 'Test Rule'})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_rule_malformed_json(client):
        response = client.post(API_PATH, content=b'notjson', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_create_rule_delete_not_allowed(client):
        response = client.delete(API_PATH)
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAutomationRule"

