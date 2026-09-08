from typing import Final

from .abstraction import IDBConstant


class DBTable(IDBConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "DBTable"
