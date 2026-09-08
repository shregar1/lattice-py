"""Regex utility dependency provider."""

from rivex import Dependency
from typing import Any, Optional

from constants import UtilityDependency
from .abstraction import IUtilityDependency
from utilities import RegexUtility
from dependencies import LoggerUtilityDependency
from utilities import Logger


class RegexUtilityDependency(IUtilityDependency):
    """
    Provides a configured :class:`RegexUtility` bound to the request context.

    Attributes:
        component: Component name stamped on every log record.
    """

    component: str = "regex_utility"


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
    ) -> RegexUtility:
        """
        Constructs a RegexUtility bound to the request context.

        Args:
            urn: Per-request unique reference identifier.
            tenant_urn: Tenant scope identifier.
            user_urn: Authenticated user identifier.
            api_name: Logical API or endpoint name.
            ip_address: Originating client IP address.
            user_agent: Originating client user-agent string.
            logger: Optional logger; if ``None``, ``LoggerUtilityDependency`` is auto-resolved.
            *args: Ignored positional args.
            **kwargs: Forwarded into RegexUtility.


        returns:
            A RegexUtility instance.
        """

        try:

            resolved_logger = logger

    
            return RegexUtility(
                urn=urn,
                tenant_urn=tenant_urn,
                user_urn=user_urn,
                api_name=api_name,
                ip_address=ip_address,
                user_agent=user_agent,
                logger=resolved_logger,
                *args,
                **kwargs,
            )

        except Exception as exc:
            logger.error('Failed to resolve dependency', exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return UtilityDependency.REGEX
