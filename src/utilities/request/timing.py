import contextvars
from typing import Any, Dict, Optional

from constants import Utility
from dtos import RequestTiming
from utilities import IRequestUtility

TimingLayer = str
_request_timing: contextvars.ContextVar[RequestTiming | None] = contextvars.ContextVar(
    "request_timing", default=None
)


class RequestTimingUtility(IRequestUtility):
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
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
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

    @staticmethod
    def begin_request() -> RequestTiming:
        ctx = RequestTiming()
        _request_timing.set(ctx)
        return ctx

    @staticmethod
    def current_request_timing() -> RequestTiming | None:
        return _request_timing.get()

    @staticmethod
    def end_request() -> None:
        _request_timing.set(None)

    @staticmethod
    def record_layer_timing(
        layer: TimingLayer, operation: str, duration_ms: float, outcome: str, **fields: Any
    ) -> None:
        ctx = _request_timing.get()
        if ctx is None:
            return
        ctx.record(layer, operation, duration_ms, outcome, **fields)

    @staticmethod
    def merge_timing_metadata(metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        merged = dict(metadata or {})
        ctx = _request_timing.get()
        if ctx is not None and ctx.spans:
            merged.update(ctx.to_metadata())
        return merged
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.REQUEST_TIMING
