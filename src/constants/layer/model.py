"""ModelName — PascalCase class-name constants for the model layer."""

from typing import Final

from .abstraction import ILayerConstant


class Model(ILayerConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Model"
