from .abstraction import IConfigurationDTO


class INotificationConfigurationDTO(IConfigurationDTO):
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
