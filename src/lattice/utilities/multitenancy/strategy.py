from lattice.utilities.multitenancy.abstraction import BaseTenantIsolationStrategy

class HeaderBasedTenantIsolationStrategy(BaseTenantIsolationStrategy):
    def resolve_tenant_id(self, context: any) -> str: return "default_tenant"
    async def apply_isolation_boundary(self, tenant_id: str, connection: any): return connection
