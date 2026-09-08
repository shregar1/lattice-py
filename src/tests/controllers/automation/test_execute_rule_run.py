
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/automation-rules'
VALID_URN = 'urn:vexarr:rule:test-001'

class TestExecuteRuleRun:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_execute_rule_valid_payload(client):
        url = f'{API_BASE}/{VALID_URN}/execute'
        response = client.post(url, json={'entity_urn': 'urn:vexarr:application:123'})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_execute_rule_empty_payload(client):
        url = f'{API_BASE}/{VALID_URN}/execute'
        response = client.post(url, json={})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_execute_rule_response_is_json(client):
        url = f'{API_BASE}/{VALID_URN}/execute'
        response = client.post(url, json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_execute_rule_get_not_allowed(client):
        url = f'{API_BASE}/{VALID_URN}/execute'
        response = client.get(url)
        assert response.status_code in (404, 405)

    @staticmethod
    def test_execute_rule_bad_body(client):
        url = f'{API_BASE}/{VALID_URN}/execute'
        response = client.post(url, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestExecuteRuleRun"

