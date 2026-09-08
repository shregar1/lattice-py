from ..abstraction import IConstant


class IAPIConstant(IConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAPIConstant"
