from lattice.exceptions.base import BaseException

class DatabaseTimeoutException(BaseException):
    def __init__(self, message: str = "Database timeout", response_key: str = "DATABASETIMEOUTEXCEPTION"):
        super().__init__(message, 504, response_key)
