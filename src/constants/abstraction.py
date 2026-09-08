from abstractions import ConstantLayer


class IConstant(ConstantLayer):
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IConstant"
