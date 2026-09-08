"""Timing-span DTO."""

from typing import Any, Dict, Optional, Self

from pydantic import Field

from .abstraction import ITimingDTO


class TimingSpanDTO(ITimingDTO):
    """A single timed operation within a layer."""

    layer: str
    operation: str
    duration_ms: float
    outcome: str
    fields: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def build(
        cls,
        layer: str,
        operation: str,
        duration_ms: float,
        outcome: str,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Self:
        cleaned = {key: value for key, value in (fields or {}).items() if value is not None}

        return cls(
            layer=layer,
            operation=operation,
            duration_ms=round(duration_ms, 2),
            outcome=outcome,
            fields=cleaned,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TimingSpanDTO"
