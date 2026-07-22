from lattice.exceptions.base import BaseException

class ConnectionFailureException(BaseException):
    def __init__(self, message: str = "Database connection failure", response_key: str = "CONNECTIONFAILUREEXCEPTION"):
        super().__init__(message, 503, response_key)
