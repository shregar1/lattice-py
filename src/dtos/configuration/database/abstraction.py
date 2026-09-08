from .abstraction import IConfigurationDTO


class IDatabaseConfigurationDTO(IConfigurationDTO):
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
