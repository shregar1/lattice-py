"""page enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Page


class PageENUM(EnumLayer):
    SIZE = Page.SIZE
    MAX_SIZE = Page.MAX_SIZE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "PageENUM"

