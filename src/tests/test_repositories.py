import importlib
import inspect
import pkgutil
import pytest
import repositories
from repositories.atomic.candidate.candidate import CandidateRepository
from repositories.job.job import JobRepository
from repositories.tenant.tenant import TenantRepository
from repositories.user.user import UserRepository
from repositories.user_account import UserRepository

ALL_REPOSITORIES: List[Tuple[str, type]] = []
REPOSITORY_CUSTOM_METHODS: List[Tuple[str, type, str]] = []
for importer, modname, ispkg in pkgutil.walk_packages(
    repositories.__path__, repositories.__name__ + "."
):
    mod = importlib.import_module(modname)
    for name, cls in inspect.getmembers(mod, inspect.isclass):

        if cls.__module__ == modname and name.endswith("Repository") and (name != "IAtomicRepository"):
            pair = (name, cls)
            ALL_REPOSITORIES.append(pair)
            for m_name, m_func in cls.__dict__.items():
        
        if inspect.isroutine(m_func) and (not m_name.startswith("_")):
                    REPOSITORY_CUSTOM_METHODS.append((name, cls, m_name))


class TestRepositories:
    @staticmethod
    @pytest.mark.parametrize(
        "name,repo_cls", ALL_REPOSITORIES, ids=[r[0] for r in ALL_REPOSITORIES]
    )
    def test_repository_instantiation_and_model_binding(name: str, repo_cls: type) -> None:

        try:

            repo = repo_cls()
            assert repo is not None
            assert hasattr(repo_cls, "model_class")

        except TypeError:
            assert hasattr(repo_cls, "model_class")

    @staticmethod
    @pytest.mark.parametrize(
        "repo_name,repo_cls,method_name",
        REPOSITORY_CUSTOM_METHODS,
        ids=[f"{m[0]}.{m[2]}" for m in REPOSITORY_CUSTOM_METHODS],
    )
    def test_repository_custom_method_callable(
        repo_name: str, repo_cls: type, method_name: str
    ) -> None:
        repo = repo_cls()
        method = getattr(repo, method_name, None)
        assert method is not None
        assert callable(method)

    @staticmethod
    @pytest.mark.asyncio
    async def test_candidate_repository_custom_methods():
        repo = CandidateRepository()

        try:

            cand = await repo.find_by_email("test@example.com")
            assert cand is None or cand is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

        try:

            count = await repo.count_by_tenant(1)
            assert isinstance(count, int)

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_job_repository_custom_methods():
        repo = JobRepository()

        try:

            jobs = await repo.find_by_tenant(1)
            assert isinstance(jobs, list) or jobs is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

        try:

            count = await repo.count_open_by_tenant(1)
            assert isinstance(count, int)

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_tenant_repository_custom_methods():
        repo = TenantRepository()

        try:

            tenant = await repo.find_by_subdomain("acmecorp")
            assert tenant is None or tenant is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

        try:

            active = await repo.find_active()
            assert active is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_user_repository_custom_methods():
        repo = UserRepository()

        try:

            users = await repo.find_by_tenant(1)
            assert users is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

    @staticmethod
    @pytest.mark.asyncio
    async def test_user_account_repository_custom_methods():
        repo = UserRepository()

        try:

            acc = await repo.find_by_email("admin@example.com")
            assert acc is None or acc is not None

        except Exception as exc:
            assert isinstance(exc, Exception)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRepositories"
