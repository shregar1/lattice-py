from lattice.exceptions.base import BaseException

class ConstraintViolationException(BaseException):
    def __init__(self, message: str = "Constraint violation", response_key: str = "CONSTRAINTVIOLATIONEXCEPTION"):
        super().__init__(message, 400, response_key)
