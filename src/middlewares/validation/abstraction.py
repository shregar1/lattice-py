import fnmatch

from abc import ABC, abstractmethod
from typing import List

from dtos import (
    RequestValidationContext,
    ResponseValidationContext,
    RuleValidationResult,
)


class IValidationRule(ABC):
    def __init__(
        self, *, exclude_paths: List[str] | None = None, exclude_methods: List[str] | None = None
    ) -> None:
        self.exclude_paths: List[str] = exclude_paths or []
        self.exclude_methods: List[str] = [m.upper() for m in exclude_methods or []]

    def is_excluded(self, path: str, method: str) -> bool:
        if method.upper() in self.exclude_methods:
            return True
        for pattern in self.exclude_paths:
            if fnmatch.fnmatch(path, pattern):
                return True
        return False

    async def validate_request(self, ctx: RequestValidationContext) -> RuleValidationResult | None:
        return None

    async def sanitize_response(self, ctx: ResponseValidationContext) -> bytes | None:
        return None
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
