from abc import ABC, abstractmethod

class BaseController(ABC):
    """Base thin HTTP controller with envelope wrappers."""
    def success(self, data, message="Success", response_key="SUCCESS"):
        return {"status": "SUCCESS", "message": message, "key": response_key, "data": data}

    def created(self, data, message="Created", response_key="RESOURCE_CREATED"):
        return {"status": "SUCCESS", "message": message, "key": response_key, "data": data}
