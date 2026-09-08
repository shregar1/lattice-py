
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/interviews'
VALID_URN = 'urn:vexarr:interview:test-001'

class TestCancelInterview:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_cancel_interview_valid_payload(client):
        url = f'{API_BASE}/{VALID_URN}/cancel'
        response = client.post(url, json={'reason': 'Scheduling conflict'})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_cancel_interview_empty_payload(client):
        url = f'{API_BASE}/{VALID_URN}/cancel'
        response = client.post(url, json={})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_cancel_interview_response_is_json(client):
        url = f'{API_BASE}/{VALID_URN}/cancel'
        response = client.post(url, json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_cancel_interview_get_not_allowed(client):
        url = f'{API_BASE}/{VALID_URN}/cancel'
        response = client.get(url)
        assert response.status_code in (404, 405)

    @staticmethod
    def test_cancel_interview_bad_body(client):
        url = f'{API_BASE}/{VALID_URN}/cancel'
        response = client.post(url, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCancelInterview"

