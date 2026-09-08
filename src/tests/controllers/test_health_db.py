
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app

class TestHealthDb:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_db_health_responds(client):
        response = client.get('/health/db')
        assert response.status_code in (200, 500)

    @staticmethod
    def test_db_health_response_is_json(client):
        response = client.get('/health/db')
        data = response.json()
        assert isinstance(data, dict)

    @staticmethod
    def test_db_health_post_not_allowed(client):
        response = client.post('/health/db', json={})
        assert response.status_code in (404, 405)

    @staticmethod
    def test_db_health_unknown_subpath(client):
        response = client.get('/health/db/unknown')
        assert response.status_code == 404

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestHealthDb"

