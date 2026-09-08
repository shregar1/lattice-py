"""Utility-layer DTOs.

Exposes the base abstraction plus concrete DTOs for logging setup options,
request/response validation contexts, request-timing, and outbox messages
and domain events.
"""

from .abstraction import IUtilityDTO
from .logger import LoggingDTO
from .timing import (
    ITimingDTO,
    RequestTiming,
    RequestTimingDTO,
    TimingSpan,
    TimingSpanDTO,
)
from .validation import (
    RequestValidationContext,
    ResponseValidationContext,
    RuleValidationResult,
)

__all__ = [
    "IUtilityDTO",
    "LoggingDTO",
    "ITimingDTO",
    "RequestTiming",
    "RequestTimingDTO",
    "TimingSpan",
    "TimingSpanDTO",
    "RequestValidationContext",
    "ResponseValidationContext",
    "RuleValidationResult",
]
