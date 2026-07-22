class MigrationRunner:
    def __init__(self): self.migrations = []
    def register(self, m): self.migrations.append(m)
    async def run_pending(self): pass
