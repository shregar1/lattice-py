from lattice.exceptions.base import BaseException

class UnauthenticatedException(BaseException):
    def __init__(self, message: str = "Unauthenticated", response_key: str = "UNAUTHENTICATEDEXCEPTION"):
        super().__init__(message, 401, response_key)
