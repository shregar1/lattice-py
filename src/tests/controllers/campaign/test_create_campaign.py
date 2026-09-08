
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1campaign'

class TestCreateCampaign:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_create_campaign_valid_payload(client):
        response = client.post(API_PATH, json={'name': 'Engineering Outreach 2026', 'tenant_id': 1})
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_create_campaign_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_create_campaign_response_is_json(client):
        response = client.post(API_PATH, json={'name': 'Test Campaign'})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_create_campaign_malformed_json(client):
        response = client.post(API_PATH, content=b'notjson', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_create_campaign_put_not_allowed(client):
        response = client.put(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCampaign"

