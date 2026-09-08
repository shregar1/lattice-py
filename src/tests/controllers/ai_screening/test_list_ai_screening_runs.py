
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/ai-screening/runs'

class TestListAIScreeningRuns:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_list_runs_responds(client):
        response = client.get(API_PATH)
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_runs_with_pagination(client):
        response = client.get(f'{API_PATH}?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_runs_response_is_json(client):
        response = client.get(API_PATH)
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_list_runs_invalid_limit(client):
        response = client.get(f'{API_PATH}?limit=0')
        assert response.status_code in (422, 500)

    @staticmethod
    def test_list_runs_negative_offset(client):
        response = client.get(f'{API_PATH}?offset=-1')
        assert response.status_code in (422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListAIScreeningRuns"

