from lattice.exceptions.base import BaseException

class UnprocessableEntityException(BaseException):
    def __init__(self, message: str = "Unprocessable entity", response_key: str = "UNPROCESSABLEENTITYEXCEPTION"):
        super().__init__(message, 422, response_key)
