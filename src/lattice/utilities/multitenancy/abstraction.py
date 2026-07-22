from abc import ABC, abstractmethod

class BaseTenantIsolationStrategy(ABC):
    @abstractmethod
    def resolve_tenant_id(self, context: any) -> str: pass
    @abstractmethod
    async def apply_isolation_boundary(self, tenant_id: str, connection: any) -> any: pass
