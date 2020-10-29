from .client import ContractsApi, ContractsApi


def initialize_routes(api):
    api.add_resource(ContractsApi, '/api/clients')
    api.add_resource(ContractApi, '/api/client/<id>')
