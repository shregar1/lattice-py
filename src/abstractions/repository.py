"""Generic repository abstraction bound to an ORM model."""

from abc import abstractmethod
from typing import Any, Optional

from .abstraction import ILayer


class RepositoryLayer(ILayer):
    """
    Base class for persistence repositories.

    Subclasses declare the db model they manage via ``model_class`` and
    inherit the standard query and mutation surface provided by
    ``repositories.abstraction.IAtomicRepository``.

    Attributes:
        model_class: The db model class handled by the repository.
        enable_soft_delete: When ``True``, deletes go through ``is_deleted``
            instead of removing the row.
        slow_query_ms: Threshold above which a query is logged as slow.
    """

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
        logger: Optional[Any] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Stores the model class and forwards request context to ``ILayer``."""

        ILayer.__init__(
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

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
