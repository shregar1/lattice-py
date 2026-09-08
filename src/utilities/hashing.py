from rivex import hash_password, verify_password, Dependency
from typing import Any, Literal, Optional

from dependencies import LoggerUtilityDependency
from enums.hashing import HashingAlgorithm
from utilities import Logger
from .abstraction import IUtility


class HashingUtility(IUtility):
    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IUtility.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            *args,
            **kwargs,
        )

        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.logger=logger

    def hash(
        self,
        password: str,
        algorithm: Literal[
            HashingAlgorithm.ARGON2, HashingAlgorithm.BCRYPT
        ] = HashingAlgorithm.ARGON2,
    ) -> str:
        """
        Method to ....
        """
        return hash_password(password, algorithm=algorithm)

    def verify(self, password: str, password_hash: str) -> bool:
        """
        Method to ....
        """
        return verify_password(password, password_hash)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "HashingUtility"
