from abc import abstractmethod

from ..abstraction import IUtilityDTO


class IOutBoxUtilityDTO(IUtilityDTO):

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
