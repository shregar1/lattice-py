from .abstraction import IDTO


class IConfigurationDTO(IDTO):
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
