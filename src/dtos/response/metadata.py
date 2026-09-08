from rivex import Field
from typing import Any, Dict, Optional, Self

from .abstraction import IDTO


class MetaDataDTO(IDTO):
    """Concrete metadata DTO used inside ``IResponseDTO.metadata``."""

    request_id: Optional[str] = None
    trace_id: Optional[str] = None
    duration_ms: Optional[float] = None
    extra: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def build(
        cls,
        request_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        duration_ms: Optional[float] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            request_id=request_id,
            trace_id=trace_id,
            duration_ms=duration_ms,
            extra=extra or {},
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "MetaDataDTO"
