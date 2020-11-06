from .contract import ContractsApi, ContractApi


def initialize_routes(api):
    api.add_resource(ContractsApi, '/api/contracts')
    api.add_resource(ContractApi, '/api/contract/<contract_id>')

