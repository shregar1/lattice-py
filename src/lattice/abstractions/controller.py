# Lattice (Python Edition) — Controller Abstraction
from abc import ABC
from typing import Any, Optional, Dict, List

class BaseController(ABC):
    """Base thin HTTP controller with standardized response envelope wrappers."""

    def envelope(
        self,
        data: Any,
        message: str = "Operation completed successfully",
        response_key: str = "SUCCESS",
        status_code: int = 200,
        context: Optional[Any] = None,
    ) -> Dict[str, Any]:
        return {
            "transactionUrn": getattr(context, "request_urn", "") if context else "",
            "status": "SUCCESS" if status_code < 400 else "FAILED",
            "responseMessage": message,
            "responseKey": response_key,
            "errors": [],
            "timestamp": getattr(context, "timestamp", None) or "",
            "metadata": {},
            "data": data,
            "referenceUrn": getattr(context, "reference_urn", "") if context else "",
        }

    def success(
        self,
        data: Any,
        message: str = "Operation completed successfully",
        response_key: str = "SUCCESS",
        context: Optional[Any] = None,
    ) -> Dict[str, Any]:
        return self.envelope(data, message, response_key, 200, context)

    def created(
        self,
        data: Any,
        message: str = "Resource created successfully",
        response_key: str = "RESOURCE_CREATED",
        context: Optional[Any] = None,
    ) -> Dict[str, Any]:
        return self.envelope(data, message, response_key, 201, context)
