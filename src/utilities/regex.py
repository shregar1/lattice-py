import re
from rivex import Dependency
from typing import Any, List, Optional, Sequence

from constants import Utility
from dependencies import LoggerUtilityDependency
from utilities import Logger
from .abstraction import IUtility


class RegexUtility(IUtility):
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

    @classmethod
    def compile_patterns(cls, patterns: Sequence[str | re.Pattern[str]]) -> List[re.Pattern[str]]:
        compiled: List[re.Pattern[str]] = []
        for p in patterns:
            if isinstance(p, re.Pattern):
                compiled.append(p)
            elif isinstance(p, str):
                compiled.append(re.compile(p, re.IGNORECASE))
        return compiled
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.REGEX
