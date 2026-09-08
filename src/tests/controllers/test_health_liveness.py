
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app

class TestHealthLiveness:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_liveness_returns_200(client):
        response = client.get('/health')
        assert response.status_code == 200

    @staticmethod
    def test_liveness_returns_ok_status(client):
        response = client.get('/health')
        data = response.json()
        assert data.get('status') == 'ok'

    @staticmethod
    def test_liveness_response_is_json(client):
        response = client.get('/health')
        assert 'application/json' in response.headers.get('content-type', '')

    @staticmethod
    def test_liveness_post_not_allowed(client):
        response = client.post('/health', json={})
        assert response.status_code in (404, 405)

    @staticmethod
    def test_liveness_delete_not_allowed(client):
        response = client.delete('/health')
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestHealthLiveness"

