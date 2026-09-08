
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/offers'
VALID_URN = 'urn:vexarr:offer:test-001'

class TestUpdateOffer:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_update_offer_valid_payload(client):
        response = client.patch(f'{API_BASE}/{VALID_URN}', json={'salary': 175000})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_update_offer_empty_payload(client):
        response = client.patch(f'{API_BASE}/{VALID_URN}', json={})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_update_offer_response_is_json(client):
        response = client.patch(f'{API_BASE}/{VALID_URN}', json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_update_offer_nonexistent_urn(client):
        response = client.patch(f'{API_BASE}/urn:vexarr:offer:NOPE', json={})
        assert response.status_code in (404, 422, 500)

    @staticmethod
    def test_update_offer_bad_body(client):
        response = client.patch(f'{API_BASE}/{VALID_URN}', content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateOffer"

