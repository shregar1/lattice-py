from typing import Self, Optional

from constants import Configuration
from .abstraction import IConfigurationDTO


class LoggingConfigurationDTO(IConfigurationDTO):
    level: str
    file: Optional[str]
    stdout: bool
    stdout_format: str
    stdout_color: str
    caller_info: bool
    sample_one_in: int

    @classmethod
    def build(
        cls,
        level: str,
        file: Optional[str],
        stdout: bool,
        stdout_format: str,
        stdout_color: str,
        caller_info: bool,
        sample_one_in: int,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            level=level,
            file=file,
            stdout=stdout,
            stdout_format=stdout_format,
            stdout_color=stdout_color,
            caller_info=caller_info,
            sample_one_in=sample_one_in,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.LOGGING
