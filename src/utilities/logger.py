import logx
import traceback

from typing import Any, Optional, Self

from .abstraction import IUtility
from constants import Utility

class LoggerUtility(IUtility):
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
        logger: Any = None,
        *args,
        **kwargs,
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
        self._kwargs = kwargs

    def trace(self, message: str, **kwargs: Any) -> None:
        logx.trace(message, **{**self._kwargs, **kwargs})

    def debug(self, message: str, **kwargs: Any) -> None:
        logx.debug(message, **{**self._kwargs, **kwargs})

    def info(self, message: str, **kwargs: Any) -> None:
        logx.info(message, **{**self._kwargs, **kwargs})

    def warn(self, message: str, **kwargs: Any) -> None:
        logx.warn(message, **{**self._kwargs, **kwargs})

    def warning(self, message: str, **kwargs: Any) -> None:
        logx.warn(message, **{**self._kwargs, **kwargs})

    def error(self, message: str, **kwargs: Any) -> None:
        logx.error(message, **{**self._kwargs, **kwargs})

    def child(self, **kwargs: Any) -> Self:
        """
        Method to ....
        """
        return self(**{**self._kwargs, **kwargs})

    def bind(self, **kwargs: Any) -> Self:
        """
        Method to ....
        """
        return self(**{**self._kwargs, **kwargs})

    def exception(self, message: str, *, exc: BaseException | None = None, **kwargs: Any) -> None:
        merged = {**self._kwargs, **kwargs}

        if exc is not None:
            merged["exception_type"] = type(exc).__name__
            merged["exception_message"] = str(exc)
            merged["stack_trace"] = "".join(
                traceback.format_exception(type(exc), exc, exc.__traceback__)
            )
        logx.error(message, **merged)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.LOGGER


Logger = LoggerUtility
