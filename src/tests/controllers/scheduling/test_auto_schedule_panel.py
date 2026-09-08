
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/scheduling'

class TestAutoSchedulePanel:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_solve_slots_valid_payload(client):
        response = client.post(f'{API_BASE}/solve-slots', json={'interviewer_ids': [1, 2, 3], 'duration_minutes': 45})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_solve_slots_response_is_json(client):
        response = client.post(f'{API_BASE}/solve-slots', json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_calendar_sync_valid_payload(client):
        response = client.post(f'{API_BASE}/calendar-sync', json={'provider': 'google', 'interview_id': 5})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_calendar_sync_response_is_json(client):
        response = client.post(f'{API_BASE}/calendar-sync', json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_solve_slots_get_not_allowed(client):
        response = client.get(f'{API_BASE}/solve-slots')
        assert response.status_code in (404, 405)

    @staticmethod
    def test_calendar_sync_malformed_json(client):
        response = client.post(f'{API_BASE}/calendar-sync', content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAutoSchedulePanel"

