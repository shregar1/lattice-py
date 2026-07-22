from lattice.exceptions.base import BaseException

class ConcurrencyConflictException(BaseException):
    def __init__(self, message: str = "Concurrency conflict", response_key: str = "CONCURRENCYCONFLICTEXCEPTION"):
        super().__init__(message, 409, response_key)
