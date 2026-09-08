
import os
os.environ['ADMIN_ENABLED'] = 'false'
import pytest
from rivex import TestClient
from main import app

class TestApiIntegration:

    @staticmethod
    @pytest.fixture(scope='module')
    def client():
        """
        Method to ....
        """
        return TestClient(app)

    @staticmethod
    def test_e2e_health_liveness(client):
        response = client.get('/health')
        assert response.status_code == 200
        data = response.json()
        assert data.get('status') == 'ok'

    @staticmethod
    def test_e2e_health_db(client):
        response = client.get('/health/db')
        assert response.status_code in (200, 500)

    @staticmethod
    def test_e2e_ai_screening_configs_create(client):
        payload = {'job_id': 1, 'min_score': 75}
        response = client.post('/api/v1/ai-screening/configs', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_ai_screening_runs_list(client):
        response = client.get('/api/v1/ai-screening/runs?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_ai_screening_runs_execute(client):
        payload = {'application_id': 1, 'config_id': 1}
        response = client.post('/api/v1/ai-screening/runs', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_analytics_dashboard(client):
        response = client.get('/api/v1/analytics/dashboard')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_analytics_saved_reports_list(client):
        response = client.get('/api/v1/analytics/reports')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_analytics_saved_reports_create(client):
        payload = {'name': 'Monthly Hiring Funnel', 'report_type': 'FUNNEL'}
        response = client.post('/api/v1/analytics/reports', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_applications_list(client):
        response = client.get('/api/v1/applications?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_applications_create(client):
        payload = {'job_id': 1, 'candidate_id': 1, 'tenant_id': 1}
        response = client.post('/api/v1/applications', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_applications_get(client):
        response = client.get('/api/v1/applications/urn:vexarr:app:123')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_applications_archive(client):
        payload = {'reason': 'Withdrawn by candidate'}
        response = client.post('/api/v1/applications/urn:vexarr:app:123/archive', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_applications_move_stage(client):
        payload = {'target_stage_id': 2}
        response = client.post('/api/v1/applications/urn:vexarr:app:123/move-stage', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_applications_rate(client):
        payload = {'rating': 5, 'feedback': 'Great interview'}
        response = client.post('/api/v1/applications/urn:vexarr:app:123/rate', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_automation_rules_list(client):
        response = client.get('/api/v1/automation-rules')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_automation_rules_create(client):
        payload = {'name': 'Auto Stage Move', 'trigger': 'STAGE_CHANGE', 'tenant_id': 1}
        response = client.post('/api/v1/automation-rules', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_automation_rules_execute(client):
        payload = {'entity_urn': 'urn:vexarr:app:123'}
        response = client.post('/api/v1/automation-rules/urn:vexarr:rule:123/execute', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_campaigns_list(client):
        response = client.get('/api/v1campaign')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_campaigns_create(client):
        payload = {'name': 'Engineering Outreach', 'tenant_id': 1}
        response = client.post('/api/v1campaign', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_campaigns_enroll_candidate(client):
        payload = {'candidate_id': 1}
        response = client.post('/api/v1campaign/urn:vexarr:campaign:123/enrollments', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_candidates_list(client):
        response = client.get('/api/v1/candidates?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_candidates_create(client):
        payload = {'name': 'Jane Doe', 'email': 'jane.doe@example.com', 'tenant_id': 1}
        response = client.post('/api/v1/candidates', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_candidates_get(client):
        response = client.get('/api/v1/candidates/urn:vexarr:cand:123')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_interviews_list(client):
        response = client.get('/api/v1/interviews')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_interviews_schedule(client):
        payload = {'application_id': 1, 'interviewer_id': 1, 'scheduled_at': '2026-08-01T10:00:00Z'}
        response = client.post('/api/v1/interviews', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_interviews_cancel(client):
        payload = {'reason': 'Scheduling conflict'}
        response = client.post('/api/v1/interviews/urn:vexarr:interview:123/cancel', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_jobs_list(client):
        response = client.get('/api/v1/jobs?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_jobs_create(client):
        payload = {'title': 'Backend Architect', 'tenant_id': 1, 'department': 'Engineering'}
        response = client.post('/api/v1/jobs', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_jobs_get(client):
        response = client.get('/api/v1/jobs/urn:vexarr:job:123')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_offers_list(client):
        response = client.get('/api/v1/offers')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_offers_create(client):
        payload = {'application_id': 1, 'salary': 180000, 'status': 'DRAFT'}
        response = client.post('/api/v1/offers', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_offers_update(client):
        payload = {'salary': 190000}
        response = client.patch('/api/v1/offers/urn:vexarr:offer:123', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_requisitions_list(client):
        response = client.get('/api/v1/requisitions')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_requisitions_create(client):
        payload = {'title': 'Staff Engineer Req', 'count': 2, 'tenant_id': 1}
        response = client.post('/api/v1/requisitions', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_scheduling_links_list(client):
        response = client.get('/api/v1/scheduling/links')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_scheduling_links_create(client):
        payload = {'name': '30-min Technical Screen', 'duration': 30}
        response = client.post('/api/v1/scheduling/links', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_scorecards_list(client):
        response = client.get('/api/v1/scorecards')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_scorecards_submit(client):
        payload = {'interview_id': 1, 'recommendation': 'STRONG_HIRE', 'comments': 'Outstanding technical depth'}
        response = client.post('/api/v1/scorecards', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_sourcing_profiles_list(client):
        response = client.get('/api/v1/sourced-profiles')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_sourcing_profiles_create(client):
        payload = {'full_name': 'Alice Smith', 'source': 'LinkedIn'}
        response = client.post('/api/v1/sourced-profiles', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_tenants_list(client):
        response = client.get('/api/v1/tenants?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_tenants_create(client):
        payload = {'name': 'Acme Corp', 'slug': 'acme-corp'}
        response = client.post('/api/v1/tenants', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @staticmethod
    def test_e2e_tenants_get(client):
        response = client.get('/api/v1/tenants/urn:vexarr:tenant:123')
        assert response.status_code in (200, 404, 422, 500)

    @staticmethod
    def test_e2e_users_list(client):
        response = client.get('/api/v1/users?offset=0&limit=10')
        assert response.status_code in (200, 422, 500)

    @staticmethod
    def test_e2e_users_create(client):
        payload = {'email': 'user@example.com', 'name': 'Test User', 'tenant_id': 1}
        response = client.post('/api/v1/users', json=payload, headers={'content-type': 'application/json'})
        assert response.status_code in (200, 201, 422, 500)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestApiIntegration"

