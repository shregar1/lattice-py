from abstractions import IConstant


class EncodingKey(IConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "EncodingKey"
