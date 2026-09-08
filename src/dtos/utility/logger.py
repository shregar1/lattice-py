"""Logging setup options DTO consumed by ``utilities.logger``."""

from pydantic import ConfigDict
from typing import Optional, Self, Tuple

from .abstraction import IUtilityDTO


class LoggingDTO(IUtilityDTO):
    """Pydantic model holding the resolved logger configuration."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    level: str
    stdout_enabled: bool
    stdout_format: str
    stdout_color: str
    log_file: Optional[str]
    log_file_gzip: bool
    sample_one_in: int
    backpressure: str
    caller_info: bool
    redact_fields: Optional[Tuple[str, ...]]

    @classmethod
    def build(
        cls,
        level: str,
        stdout_enabled: bool,
        stdout_format: str,
        stdout_color: str,
        log_file: Optional[str],
        log_file_gzip: bool,
        sample_one_in: int,
        backpressure: str,
        caller_info: bool,
        redact_fields: Optional[Tuple[str, ...]] = None,
    ) -> Self:
        """Build from a dict, dataclass, or kwargs; ``None`` yields defaults."""

        return cls(
            level=level,
            stdout_enabled=stdout_enabled,
            stdout_format=stdout_format,
            stdout_color=stdout_color,
            log_file=log_file,
            log_file_gzip=log_file_gzip,
            sample_one_in=sample_one_in,
            backpressure=backpressure,
            caller_info=caller_info,
            redact_fields=redact_fields,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "LoggingDTO"
