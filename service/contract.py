""" Class representing a contract
    """
class Contract():

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

   # def validate_contract(self,contract_id):
        """ validar contrato"""
    #    return (self.contract_id=contract_id and self.state="ACTIVO" and (len(self.beneficiary >0) 
        
        
    def add_beneficiary(self, id_beneficiary):
        """ Incluir beneficiario"""
        self.beneficiary.append(id_beneficiary)
        return len(self.beneficiary) - 1


    def get_all_beneficiary(self):
        """ Consultar los beneficiarios"""
        return self.beneficiary
                                                                          
    def get_beneficiary(self, p_index):
        """ Consultar beneficiario"""
        if p_index >= len(self.beneficiary):
            return 'There is no such preexistence'
        return self.beneficiary[p_index]

    def delete_beneficiary(self, beneficiary):
        """ Elimina beneficiario"""
        self.beneficiary.remove(beneficiary)
        return len(self.beneficiary) - 1

    
if __name__ == '__main__':
    contract_instance = Contract('123', '10', 'COLSANITAS', 'A', 'Perez', 'Pablo', '147852')
    print('Contract 123 has been added')
