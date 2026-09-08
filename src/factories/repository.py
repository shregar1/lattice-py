from typing import Dict, Any, Type
from abstractions import IFactory
from abstractions import IAtomicRepository
from constants import Repository
from repositories import AuthTypeLKRepository
from repositories import MFATypeLKRepository
from repositories import OtpTypeLKRepository
from repositories import TenantRepository
from repositories import TenantProfileRepository
from repositories import UserRepository
from repositories import UserOtpRepository
from repositories import UserRecoveryCodeRepository
from repositories import UserTypeLKRepository


class RepositoryFactory(IFactory[IAtomicRepository[Any, Any]]):
    _registry: Dict[str, Type[IAtomicRepository[Any, Any]]] = {
        Repository.TENANT: TenantRepository,
        Repository.TENANT_PROFILE: TenantProfileRepository,
        Repository.USER: UserRepository,
        Repository.USER_OTP: UserOtpRepository,
        Repository.USER_RECOVERY_CODE: UserRecoveryCodeRepository,
        Repository.USER_TYPE_LK: UserTypeLKRepository,
    }

    def get(self, repo_name: str, **overrides: Any) -> IAtomicRepository[Any, Any]:
        key = repo_name.lower()

        if key not in self._registry:
            raise KeyError(
                f"Unknown repository name: '{repo_name}'. Available: {list(self._registry.keys())}"
            )
        repo_cls = self._registry[key]

        return repo_cls(**overrides)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RepositoryFactory"
