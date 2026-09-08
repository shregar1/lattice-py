from abstractions import IConstant


class IDBConstant(IConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDBConstant"
