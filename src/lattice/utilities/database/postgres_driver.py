from lattice.utilities.database.driver import IDatabaseDriver

class PostgresDriver(IDatabaseDriver):
    def __init__(self, config: dict = None):
        self.config = config or {}
        self._connected = False

    async def connect(self) -> None: self._connected = True
    async def disconnect(self) -> None: self._connected = False
    async def query(self, sql: str, params = None): return []
    async def begin_transaction(self): return self
    async def health_check(self) -> bool: return self._connected
    def get_driver_name(self) -> str: return "postgres"
