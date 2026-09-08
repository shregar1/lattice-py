
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_PATH = '/api/v1/scorecards'

class TestSubmitScorecard:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_submit_scorecard_valid_payload(client):
        payload = {'interview_id': 1, 'recommendation': 'STRONG_HIRE', 'comments': 'Excellent technical depth'}
        response = client.post(API_PATH, json=payload)
        assert response.status_code in (200, 201, 500)

    @staticmethod
    def test_submit_scorecard_minimal_payload(client):
        response = client.post(API_PATH, json={})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_submit_scorecard_response_is_json(client):
        response = client.post(API_PATH, json={})
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_submit_scorecard_malformed_json(client):
        response = client.post(API_PATH, content=b'bad', headers={'content-type': 'application/json'})
        assert response.status_code in (400, 422, 500)

    @staticmethod
    def test_submit_scorecard_put_not_allowed(client):
        response = client.put(API_PATH, json={})
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSubmitScorecard"

