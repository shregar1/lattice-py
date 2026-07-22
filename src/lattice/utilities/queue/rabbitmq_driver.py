from lattice.utilities.queue.abstraction import BaseQueueClient

class RabbitMQQueueDriver(BaseQueueClient):
    def __init__(self, config: dict = None): self.config = config or {}
    async def publish(self, topic: str, payload: any) -> str: return "amqp_123"
    async def subscribe(self, topic: str, handler): pass
    def get_driver_name(self) -> str: return "rabbitmq"
