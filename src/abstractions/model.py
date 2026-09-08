"""Base class for ORM-backed persistence models."""

from abc import ABC, abstractmethod
from ormx import Model
from typing import Any, Self


class ModelLayer(Model, ABC):
    """
    Base class for db persistence models.

    Subclasses must implement :meth:`build` as a typed factory that constructs
    an instance from named arguments. The db ``Model`` superclass provides
    field declaration, persistence and query helpers.
    """

    @abstractmethod
    def build(cls, **kwargs: Any) -> Self:
        """Constructs a fully-populated model instance from named arguments."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
