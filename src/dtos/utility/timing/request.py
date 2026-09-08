"""Request-timing DTO."""

import time

from pydantic import Field
from typing import Any, Dict, List, Self

from .abstraction import ITimingDTO
from .span import TimingSpanDTO
from constants import ILayerConstant as Layer


class RequestTimingDTO(ITimingDTO):
    """Aggregate timing context for one request lifecycle."""

    started_at: float = Field(default_factory=time.perf_counter)
    spans: List[TimingSpanDTO] = Field(default_factory=list)

    def record(
        self,
        layer: str,
        operation: str,
        duration_ms: float,
        outcome: str,
        **fields: Any,
    ) -> None:
        cleaned = {key: value for key, value in fields.items() if value is not None}
        self.spans.append(
            TimingSpanDTO.build(
                layer=layer,
                operation=operation,
                duration_ms=duration_ms,
                outcome=outcome,
                fields=cleaned,
            )
        )

    def to_metadata(self) -> Dict[str, Any]:
        layers: Dict[str, Any] = {
            layer: {
                "duration_ms": 0.0,
                "count": 0,
                "spans": []
            } for layer in Layer.LAYERS
        }
        for span in self.spans:
            bucket = layers[span.layer]
            bucket["duration_ms"] = round(bucket["duration_ms"] + span.duration_ms, 2)
            bucket["count"] += 1
            bucket["spans"].append(
                {
                    "operation": span.operation,
                    "duration_ms": span.duration_ms,
                    "outcome": span.outcome,
                    **span.fields,
                }
            )
        wall_ms = round((time.perf_counter() - self.started_at) * 1000, 2)
        http_ms = layers["http"]["duration_ms"] or wall_ms

        return {
            "timing": {
                "total_ms": wall_ms,
                "http_ms": http_ms,
                "layers": layers
            }
        }

    @classmethod
    def build(cls, *args: Any, **kwargs: Any) -> Self:
        """Constructs a fully-validated instance from the given inputs."""
        return cls(*args, **kwargs)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestTimingDTO"
