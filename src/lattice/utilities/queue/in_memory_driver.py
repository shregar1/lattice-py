from lattice.utilities.queue.abstraction import BaseQueueClient

class InMemoryQueueDriver(BaseQueueClient):
    def __init__(self): self._handlers = {}
    async def publish(self, topic: str, payload: any) -> str: return "msg_123"
    async def subscribe(self, topic: str, handler): self._handlers[topic] = handler
    def get_driver_name(self) -> str: return "in_memory"
