""" Class representing a client
    """
class Client():

    def __init__(self, contract_id, plan, insurance_name,state,last_name,principal_name,principal_id):
        """ init contract"""
        self.contract_id = contract_id
        self.plan = plan
        self.insurance_name = insurance_name
        self.state = state
        self.last_name = last_name
        self.principal_name = principal_name
        self.principal_id = principal_id
        self.beneficiary = []

    def add_beneficiary(self, id_beneficiary):
        """ Incluir beneficiario"""
        self.beneficiary.append(id_beneficiary)
        return len(self.beneficiary) - 1


    def get_all_beneficiary(self):
        """ Consultar los beneficiarios"""
        return self.beneficiary

    def delete_beneficiary(self, id_beneficiary):
        """ Elimina beneficiario"""
        self.beneficiary.remove(id_beneficiary)
        return len(self.id_beneficiary) - 1

    
if __name__ == '__main__':
    contract_instance = contract('123', '10', 'COLSANITAS', 'A', 'Perez', 'Pablo', '147852')
    print('Contract 123 has been added')
