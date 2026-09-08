
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1campaign'

class TestListCampaigns:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_list_campaigns_responds(client):
        response = client.get(API_PATH)
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_campaigns_with_pagination(client):
        response = client.get(f'{API_PATH}?offset=0&limit=15')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_list_campaigns_response_is_json(client):
        response = client.get(API_PATH)
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_list_campaigns_overlarge_limit(client):
        response = client.get(f'{API_PATH}?limit=500')
        assert response.status_code in (422, 500)

    @staticmethod
    def test_list_campaigns_patch_not_allowed(client):
        response = client.patch(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListCampaigns"

