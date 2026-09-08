"""Repository abstraction layer.

Concrete repositories inherit from ``IRepository`` and only set
``model_class``; the 18 base methods (filter, find_by_id, create, ...) are
implemented here against the ormx model API.
"""

from abc import ABC, abstractmethod
from rivex import Dependency
from typing import Any, Optional

from abstractions import RepositoryLayer
from dependencies import LoggerUtilityDependency
from utilities import Logger


class IRepository(RepositoryLayer, ABC):
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
        RepositoryLayer.__init__(
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
            **kwargs,
        )

    @abstractmethod
    @property
    def name(self) -> str:
        pass
