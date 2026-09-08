from typing import Final

from .abstraction import ILayerConstant


class Service(ILayerConstant):


    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Service"
