from ..abstraction import IConstant


class IConfigurationConstant(IConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IConfigurationConstant"
