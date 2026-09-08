"""PascalCase class-name constants for the abstraction layer."""

from typing import Final, Tuple

from abstractions import ConstantLayer


class ILookupConstant(ConstantLayer):
    """Base abstraction for lookup constant classes."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ILookupConstant"
