from lattice.utilities.database.driver import IDatabaseDriver

class SqliteDriver(IDatabaseDriver):
    def __init__(self, file_path: str = ":memory:"):
        self.file_path = file_path
        self._connected = False

    async def connect(self) -> None: self._connected = True
    async def disconnect(self) -> None: self._connected = False
    async def query(self, sql: str, params = None): return []
    async def begin_transaction(self): return self
    async def health_check(self) -> bool: return self._connected
    def get_driver_name(self) -> str: return "sqlite"
