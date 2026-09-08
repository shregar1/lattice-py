"""Lookup repository abstraction layer."""

from abc import ABC
from typing import Any, Dict, List, Optional, Sequence

from rivex import Dependency

from dependencies.utility import LoggerUtilityDependency
from models import IModel
from utilities import Logger

from ..abstraction import IAtomicRepository


class ILookupRepository(IAtomicRepository[IModel, int], ABC):
    """Base class for lookup (reference/type table) repositories."""

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
        model: IModel = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IAtomicRepository.__init__(
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
        self.model = model
        self.model_class = model

    def find_by_code(self, code: str) -> Optional[IModel]:
        """Find a lookup record by its unique code."""
        results = self.filter("code", code)
        return results[0] if results else None

    def find_by_codes(self, codes: Sequence[str]) -> List[IModel]:
        """Find lookup records matching a list of codes."""
        if not codes:
            return []
        return self.filter_in("code", codes)

    def exists_by_code(self, code: str) -> bool:
        """Check if a lookup record exists with the given code."""
        return self.find_by_code(code) is not None

    def get_code_map(self) -> Dict[str, IModel]:
        """Returns a dictionary mapping lookup code -> model instance."""
        return {
            getattr(item, "code"): item
            for item in self.list_all()
            if hasattr(item, "code")
        }

    def get_id_by_code(self, code: str) -> Optional[int]:
        """Resolves the primary key ID for a given lookup code."""
        item = self.find_by_code(code)
        return getattr(item, "id", None) if item is not None else None
