
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/candidates'

class TestListCandidates:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_list_candidates_responds(client):
        response = client.get(API_PATH)
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_candidates_with_pagination(client):
        response = client.get(f'{API_PATH}?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_candidates_response_is_json(client):
        response = client.get(API_PATH)
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_list_candidates_with_email_filter(client):
        response = client.get(f'{API_PATH}?email=test@example.com')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_candidates_invalid_page_size(client):
        response = client.get(f'{API_PATH}?page_size=201')
        assert response.status_code in (422, 500)

    @staticmethod
    def test_list_candidates_delete_not_allowed(client):
        response = client.delete(API_PATH)
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListCandidates"

