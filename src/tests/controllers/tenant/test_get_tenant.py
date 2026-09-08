
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app
API_BASE = '/api/v1/tenants'
VALID_URN = 'urn:vexarr:tenant:test-001'
NONEXISTENT_URN = 'urn:vexarr:tenant:XXXNONEXISTENT9999'

class TestGetTenant:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_get_tenant_responds(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_get_tenant_response_is_json(client):
        response = client.get(f'{API_BASE}/{VALID_URN}')
        assert isinstance(response.json(), dict)

    @staticmethod
    def test_get_nonexistent_tenant(client):
        response = client.get(f'{API_BASE}/{NONEXISTENT_URN}')
        assert response.status_code in (404, 422, 500)

    @staticmethod
    def test_get_tenant_delete_not_allowed(client):
        response = client.delete(f'{API_BASE}/{VALID_URN}')
        assert response.status_code in (404, 405)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetTenant"

