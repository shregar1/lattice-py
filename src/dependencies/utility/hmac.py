"""HMAC utility dependency provider."""

from rivex import Dependency
from typing import Any, Optional

from .abstraction import IUtilityDependency
from constants import UtilityDependency
from dependencies import LoggerUtilityDependency
from utilities import HMACUtility
from utilities import Logger


class HMACUtilityDependency(IUtilityDependency):

    def resolve(
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
    ) -> HMACUtility:

        try:
            return HMACUtility(
                urn=urn,
                tenant_id=tenant_id,
                tenant_urn=tenant_urn,
                user_id=user_id,
                user_urn=user_urn,
                api_name=api_name,
                ip_address=ip_address,
                user_agent=user_agent,
                logger=logger,
                **kwargs,
            )

        except Exception as exc:
            logger.error("Failed to resolve dependency", exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return UtilityDependency.HMAC
