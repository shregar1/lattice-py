"""Abstraction for dependency layer constant classes."""

from ..abstraction import ILayerConstant


class IDependencyConstant(ILayerConstant):
    """Base abstraction for dependency layer constant classes."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDependencyConstant"
