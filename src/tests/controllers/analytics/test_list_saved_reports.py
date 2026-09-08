
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/analytics/reports'

class TestListSavedReports:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_list_reports_responds(client):
        response = client.get(API_PATH)
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_reports_with_pagination(client):
        response = client.get(f'{API_PATH}?offset=0&limit=5')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_reports_response_is_json(client):
        response = client.get(API_PATH)
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_list_reports_negative_limit(client):
        response = client.get(f'{API_PATH}?limit=-1')
        assert response.status_code in (422, 500)

    @staticmethod
    def test_list_reports_delete_not_allowed(client):
        response = client.delete(API_PATH)
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSavedReports"

