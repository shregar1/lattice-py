from .abstraction import IConstant
from typing import Final


class Log(IConstant):

    APP_STARTED: Final[str] = "app_started"
    APP_SHUTDOWN: Final[str] = "app_shutdown"
    CONTROLLER_STARTED: Final[str] = "controller_started"
    CONTROLLER_COMPLETED: Final[str] = "controller_completed"
    CONTROLLER_FAILED: Final[str] = "controller_failed"
    REQUEST_STARTED: Final[str] = "request_started"
    REQUEST_COMPLETED: Final[str] = "request_completed"
    REQUEST_FAILED: Final[str] = "request_failed"
    DB_QUERY_SLOW: Final[str] = "db_query_slow"
    REPOSITORY_STARTED: Final[str] = "repository_started"
    REPOSITORY_COMPLETED: Final[str] = "repository_completed"
    REPOSITORY_FAILED: Final[str] = "repository_failed"
    REPOSITORY_OPERATION: Final[str] = "repository_operation"
    SERVICE_STARTED: Final[str] = "service_started"
    SERVICE_COMPLETED: Final[str] = "service_completed"
    SERVICE_FAILED: Final[str] = "service_failed"
    UTILITY_STARTED: Final[str] = "utility_started"
    UTILITY_COMPLETED: Final[str] = "utility_completed"
    UTILITY_FAILED: Final[str] = "utility_failed"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Log"
