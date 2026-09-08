"""Timing utility DTOs package."""

from .abstraction import ITimingDTO
from .request import RequestTimingDTO
from .span import TimingSpanDTO

# Backward compatibility aliases
RequestTiming = RequestTimingDTO
TimingSpan = TimingSpanDTO

__all__ = [
    "ITimingDTO",
    "RequestTimingDTO",
    "TimingSpanDTO",
    "RequestTiming",
    "TimingSpan",
]
