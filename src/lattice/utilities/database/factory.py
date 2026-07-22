import os
from lattice.utilities.database.sqlite_driver import SqliteDriver
from lattice.utilities.database.postgres_driver import PostgresDriver

class DatabaseDriverFactory:
    @staticmethod
    def create_driver(config: dict = None):
        config = config or {}
        db_type = config.get("type") or os.getenv("DATABASE_TYPE", "sqlite")
        if db_type.lower() in ["postgres", "postgresql", "pg"]:
            return PostgresDriver(config.get("postgres"))
        return SqliteDriver(config.get("sqlite_path", ":memory:"))
