import secrets
import string
import ulid

from rivex import Dependency
from typing import Any, Optional
from uuid import UUID, uuid4

from .abstraction import IUtility
from dependencies import LoggerUtilityDependency
from utilities import Logger


class URNUtility(IUtility):
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

    @staticmethod
    def generate_uuid4() -> UUID:
        """
        Method to ....
        """
        return uuid4()

    @staticmethod
    def generate_uuid() -> str:
        """
        Method to ....
        """
        return str(uuid4())

    @staticmethod
    def generate_ulid() -> str:
        """
        Method to ....
        """
        return ulid.new().str

    def generate_random_string(self, length: int) -> str:
        """
        Method to ....
        """
        return "".join(
            (secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        )

    def generate_urn(self, prefix: str) -> str:
        """
        Method to ....
        """
        return f"urn:{prefix}:{self.generate_uuid4().hex}"

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "URNUtility"


__all__ = ["URNUtility"]
