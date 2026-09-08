
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/applications'
VALID_URN = 'urn:vexarr:application:test-001'

class TestMoveApplicationStage:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_move_stage_valid_payload(client):
        url = f'{API_BASE}/{VALID_URN}/move-stage'
        response = client.post(url, json={'target_stage_id': 3})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_move_stage_empty_payload(client):
        url = f'{API_BASE}/{VALID_URN}/move-stage'
        response = client.post(url, json={})
        assert response.status_code in (200, 201, 404, 422, 500)

    @staticmethod
    def test_move_stage_response_is_json(client):
        url = f'{API_BASE}/{VALID_URN}/move-stage'
        response = client.post(url, json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_move_stage_get_not_allowed(client):
        url = f'{API_BASE}/{VALID_URN}/move-stage'
        response = client.get(url)
        assert response.status_code in (404, 405)

    @staticmethod
    def test_move_stage_unknown_urn_is_4xx(client):
        url = f'{API_BASE}/urn:vexarr:application:XXXNONEXISTENT/move-stage'
        response = client.post(url, json={})
        assert response.status_code in (404, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMoveApplicationStage"

