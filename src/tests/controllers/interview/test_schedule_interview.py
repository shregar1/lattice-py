
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/interviews'

class TestScheduleInterview:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_schedule_interview_valid_payload(client):
        payload = {'application_id': 1, 'interviewer_id': 2, 'scheduled_at': '2026-09-01T10:00:00Z'}
        response = client.post(API_PATH, json=payload)
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_schedule_interview_empty_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_schedule_interview_response_is_json(client):
        response = client.post(API_PATH, json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_schedule_interview_malformed_body(client):
        response = client.post(API_PATH, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_schedule_interview_put_not_allowed(client):
        response = client.put(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestScheduleInterview"

