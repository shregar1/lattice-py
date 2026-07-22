class SeederRunner:
    def __init__(self): self.seeders = []
    def register(self, s): self.seeders.append(s)
    async def run_all(self): pass
