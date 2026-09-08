"""Base class for Pydantic-based request and response DTOs."""

from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any, Self


class DTOLayer(BaseModel, ABC):
    """
    Base class for request and response data-transfer objects.

    Inherits from Pydantic's ``IModel`` with ``extra`` fields forbidden and
    population by field name enabled. Subclasses must implement :meth:`build`
    to provide a typed factory that constructs the DTO from raw inputs.
    """

    model_config = {"extra": "forbid", "populate_by_name": True}

    @classmethod
    @abstractmethod
    def build(cls, *args: Any, **kwargs: Any) -> Self:
        """Constructs a fully-validated instance from the given inputs."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
