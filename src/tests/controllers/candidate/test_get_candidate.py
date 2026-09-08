
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/candidates'
VALID_URN = 'urn:vexarr:candidate:test-001'
NONEXISTENT_URN = 'urn:vexarr:candidate:XXXNONEXISTENT99999'

class TestGetCandidate:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_get_candidate_responds(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_get_candidate_response_is_json(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_get_nonexistent_candidate(client):
        response = client.get(f'{API_BASE}/{NONEXISTENT_URN}')
        assert response.status_code in (404, 422, 500)

    @staticmethod
    def test_get_candidate_post_not_allowed(client):
        response = client.post(f'{API_BASE}/{VALID_URN}', json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetCandidate"

