from typing import Self

from constants import Configuration
from .abstraction import IConfigurationDTO


class PathConfigurationDTO(IConfigurationDTO):
    logs_dir: str
    migrations_dir: str
    scripts_dir: str
    media_dir: str
    media_url_prefix: str

    @classmethod
    def build(
        cls,
        logs_dir: str,
        migrations_dir: str,
        scripts_dir: str,
        media_dir: str,
        media_url_prefix: str,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            logs_dir=logs_dir,
            migrations_dir=migrations_dir,
            scripts_dir=scripts_dir,
            media_dir=media_dir,
            media_url_prefix=media_url_prefix,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.PATH
