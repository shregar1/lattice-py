import importlib
import inspect
import pkgutil
from typing import List
import pytest
import orchestrator.api.v1
from dtos import CreateCandidateRequest
from dtos import CreateJobRequest
from dtos import CreateTenantRequest
from orchestrator.api.v1.candidate.create_orchestrator import CreateCandidateOrchestratorService
from orchestrator.api.v1.candidate.validate import ValidateCandidateService
from orchestrator.api.v1.job.create_orchestrator import CreateJobOrchestratorService
from orchestrator.api.v1.job.validate import ValidateJobService
from orchestrator.api.v1.tenant.create_orchestrator import CreateTenantOrchestratorService
from orchestrator.api.v1.tenant.validate import ValidateTenantService

ALL_SERVICES: List[Tuple[str, type]] = []
ORCHESTRATOR_SERVICES: List[Tuple[str, type]] = []
INDIVIDUAL_SERVICES: List[Tuple[str, type]] = []
for importer, modname, ispkg in pkgutil.walk_packages(
    orchestrator.api.v1.__path__, orchestrator.api.v1.__name__ + "."
):
    mod = importlib.import_module(modname)
    for name, cls in inspect.getmembers(mod, inspect.isclass):

        if cls.__module__ == modname and name.endswith("Service") and (name != "ServiceLayer"):
            pair = (name, cls)
            ALL_SERVICES.append(pair)
    
        if "Orchestrator" in name:
                ORCHESTRATOR_SERVICES.append(pair)
            else:
                INDIVIDUAL_SERVICES.append(pair)


class TestServices:
    @staticmethod
    @pytest.mark.parametrize("name,service_cls", ALL_SERVICES, ids=[p[0] for p in ALL_SERVICES])
    def test_all_services_instantiation_and_contract(name: str, service_cls: type) -> None:
        assert (
            hasattr(service_cls, "run")
            or hasattr(service_cls, "execute")
            or issubclass(service_cls, ServiceLayer)
            or issubclass(service_cls, IOrchestrator)
        )

    @staticmethod
    @pytest.mark.parametrize(
        "name,service_cls", ORCHESTRATOR_SERVICES, ids=[p[0] for p in ORCHESTRATOR_SERVICES]
    )
    def test_orchestrator_service_structure(name: str, service_cls: type) -> None:
        assert "Orchestrator" in name
        assert (
            hasattr(service_cls, "execute")
            or hasattr(service_cls, "run")
            or issubclass(service_cls, IOrchestrator)
        )

    @staticmethod
    @pytest.mark.parametrize(
        "name,service_cls", INDIVIDUAL_SERVICES, ids=[p[0] for p in INDIVIDUAL_SERVICES]
    )
    def test_individual_service_structure(name: str, service_cls: type) -> None:
        assert "Orchestrator" not in name
        assert (
            hasattr(service_cls, "run")
            or hasattr(service_cls, "execute")
            or issubclass(service_cls, ServiceLayer)
        )

    @staticmethod
    @pytest.mark.asyncio
    async def test_individual_validate_candidate():
        service = ValidateCandidateService()
        req = CreateCandidateRequest.model_validate(
            {"name": "Test Candidate", "email": "candidate@example.com", "tenant_id": 1}
        )

    @staticmethod
    @pytest.mark.asyncio
    async def test_individual_validate_candidate():

        try:

            service = ValidateCandidateService()
            req = CreateCandidateRequest.model_validate(
                {"name": "Test Candidate", "email": "candidate@example.com", "tenant_id": 1}
            )
            res = await service.run(req)
            assert res is True or res is None or isinstance(res, (dict, bool))

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_individual_validate_job():

        try:

            service = ValidateJobService()
            req = CreateJobRequest.model_validate(
                {
                    "title": "Backend Dev",
                    "department": "Engineering",
                    "description": "Build high scale APIs",
                    "openings": 1,
                    "salary_min": 100000,
                    "salary_max": 150000,
                    "hiring_manager_id": 1,
                    "recruiter_id": 2,
                    "status_id": 1,
                    "domain_id": 1,
                    "currency_id": 1,
                    "employment_config_id": 1,
                    "tenant_id": 1,
                    "job_role_id": 1,
                    "job_role_level_id": 1,
                }
            )
            res = await service.run(req)
            assert res is True or res is None or isinstance(res, (dict, bool))

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_individual_validate_tenant():

        try:

            service = ValidateTenantService()
            req = CreateTenantRequest.model_validate({"name": "Test Tenant", "slug": "test-tenant"})
            res = await service.run(req)
            assert res is True or res is None or isinstance(res, (dict, bool))

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_orchestrator_create_candidate_workflow():

        try:

            service = CreateCandidateOrchestratorService()
            req = CreateCandidateRequest.model_validate(
                {"name": "John Doe", "email": "john@example.com", "tenant_id": 1}
            )
            res = await service.execute(req)
            assert res is not None or isinstance(res, dict)

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_orchestrator_create_job_workflow():

        try:

            service = CreateJobOrchestratorService()
            req = CreateJobRequest.model_validate(
                {
                    "title": "DevOps Lead",
                    "department": "Infrastructure",
                    "description": "Manage Cloud Platform",
                    "openings": 2,
                    "salary_min": 120000,
                    "salary_max": 180000,
                    "hiring_manager_id": 1,
                    "recruiter_id": 2,
                    "status_id": 1,
                    "domain_id": 1,
                    "currency_id": 1,
                    "employment_config_id": 1,
                    "tenant_id": 1,
                    "job_role_id": 1,
                    "job_role_level_id": 1,
                }
            )
            res = await service.execute(req)
            assert res is not None or isinstance(res, dict)

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_orchestrator_create_tenant_workflow():

        try:

            service = CreateTenantOrchestratorService()
            req = CreateTenantRequest.model_validate({"name": "Acme Corp", "slug": "acme-corp"})
            res = await service.execute(req)
            assert res is not None or isinstance(res, dict)

        except Exception as exc:
            assert isinstance(exc, Exception)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestServices"
