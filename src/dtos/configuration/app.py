from typing import Self

from constants import Configuration
from .abstraction import IConfigurationDTO


class AppConfigurationDTO(IConfigurationDTO):
    name: str
    powered_by: str
    host: str
    port: int
    cors_origin: str
    rate_limit_max: int
    rate_limit_window_seconds: int
    debug: bool
    request_timeout: int

    @classmethod
    def build(
        cls,
        name: str,
        powered_by: str,
        host: str,
        port: int,
        cors_origin: str,
        rate_limit_max: int,
        rate_limit_window_seconds: int,
        debug: bool,
        request_timeout: int,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            name=name,
            powered_by=powered_by,
            host=host,
            port=port,
            cors_origin=cors_origin,
            rate_limit_max=rate_limit_max,
            rate_limit_window_seconds=rate_limit_window_seconds,
            debug=debug,
            request_timeout=request_timeout,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.APP
