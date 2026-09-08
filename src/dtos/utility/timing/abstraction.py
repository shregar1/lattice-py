"""Base abstraction for timing utility DTOs."""

from abc import abstractmethod
from typing import Any, Self

from dtos import IUtilityDTO


class ITimingDTO(IUtilityDTO):
    """Marker base for timing utility DTOs."""

    @classmethod
    def build(cls, *args: Any, **kwargs: Any) -> Self:
        """Constructs a fully-validated instance from the given inputs."""
        return cls(*args, **kwargs)

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass


__all__ = ["ITimingDTO"]
