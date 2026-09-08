from ..abstraction import IConfigurationConstant


class IDatabaseConfigurationConstant(IConfigurationConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDatabaseConfigurationConstant"
