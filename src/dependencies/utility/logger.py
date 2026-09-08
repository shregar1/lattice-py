"""Logger utility dependency provider."""

from rivex import Dependency
from typing import Any, Optional

from constants import UtilityDependency
from .abstraction import IUtilityDependency
from utilities import LoggerUtility


class LoggerUtilityDependency(IUtilityDependency):
    """
    Provides a configured :class:`LoggerUtility` for the current request context.

    The logger sits at the top of the dependency chain — every other utility
    dependency that accepts a ``logger`` argument depends on this one.

    Attributes:
        component: Logger component name stamped on every log record.
    """


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
        *args: Any,
        **kwargs: Any,
    ) -> LoggerUtility:
        """
        Constructs a LoggerUtility bound to the request context fields.

        Args:
            urn: Per-request unique reference identifier.
            tenant_urn: Tenant scope identifier.
            user_urn: Authenticated user identifier.
            api_name: Logical API or endpoint name.
            ip_address: Originating client IP address.
            user_agent: Originating client user-agent string.
            logger: Optional parent logger to inherit fields from.
            *args: Ignored positional args.
            **kwargs: Forwarded into LoggerUtility as bound fields.


        returns:
            A LoggerUtility instance ready to emit structured records.
        """

        try:
            return LoggerUtility(
                urn=urn,
                tenant_urn=tenant_urn,
                user_urn=user_urn,
                api_name=api_name,
                ip_address=ip_address,
                user_agent=user_agent,
                *args,
                **kwargs,
            )

        except Exception as exc:
            logger.error('Failed to resolve dependency', exc=exc)
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return UtilityDependency.LOGGER
