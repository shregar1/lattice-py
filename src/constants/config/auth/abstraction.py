from ..abstraction import IConfigurationConstant


class IAuthConfigurationConstant(IConfigurationConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAuthConfigurationConstant"
