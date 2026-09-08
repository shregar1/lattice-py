"""Enum base with value/name lookup helpers."""

from abc import abstractmethod
from enum import Enum
from typing import Any, List


class EnumLayer(Enum):
    """
    Base enum with helpers for working with member values and names.

    Provides classmethods for listing values and names and for membership
    checks by value, which keeps callers from reaching into ``Enum`` internals.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass

    @classmethod
    def values(cls) -> List[Any]:
        """Returns the list of member values declared on the enum."""
        return [member.value for member in cls]

    @classmethod
    def names(cls) -> List[str]:
        """Returns the list of member names declared on the enum."""
        return [member.name for member in cls]

    @classmethod
    def has_value(cls, value: Any) -> bool:
        """Returns ``True`` when ``value`` matches one of the enum's values."""
        return value in cls.values()
