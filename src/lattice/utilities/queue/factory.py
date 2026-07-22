import os
from lattice.utilities.queue.in_memory_driver import InMemoryQueueDriver
from lattice.utilities.queue.rabbitmq_driver import RabbitMQQueueDriver

class QueueClientFactory:
    @staticmethod
    def create_client(config: dict = None):
        config = config or {}
        q_type = config.get("type") or os.getenv("QUEUE_TYPE", "in_memory")
        if q_type.lower() in ["rabbitmq", "amqp"]: return RabbitMQQueueDriver(config.get("rabbitmq"))
        return InMemoryQueueDriver()
