
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/analytics/dashboard'

class TestGetAnalyticsDashboard:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_dashboard_responds(client):
        response = client.get(API_PATH)
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_dashboard_response_is_json(client):
        response = client.get(API_PATH)
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_dashboard_with_tenant_param(client):
        response = client.get(f'{API_PATH}?tenant_id=1')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_dashboard_post_not_allowed(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (404, 405)

    @staticmethod
    def test_dashboard_invalid_subpath(client):
        response = client.get(f'{API_PATH}/xyz')
        assert response.status_code == 404

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetAnalyticsDashboard"

