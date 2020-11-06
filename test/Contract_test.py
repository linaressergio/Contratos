import unittest

from service.contract import Contract


class ContractTestCase(unittest.TestCase):
    def setUp(self):
        self.test_contract = Contract('123', '10', 'COLSANITAS', 'ACTIVO', 'Perez', 'Pablo', '147852')

    #def test_validate_contract(self):
     #   self.assertEqual(self.test_contract.validate_contract(self.test_contract,123),true)
    
    def test_name_add_beneficiary(self):
        self.assertEqual(len(self.test_contract.get_all_beneficiary()), 0)
        
        self.test_contract.add_beneficiary('mock beneficiary')
        self.assertEqual(len(self.test_contract.get_all_beneficiary()), 1)
        
        self.assertEqual(self.test_contract.get_beneficiary(0), 'mock beneficiary')
        self.assertEqual(self.test_contract.get_beneficiary(1), 'There is no such beneficiary')
        
    def test_name_delete_beneficiary(self):
        self.assertEqual(len(self.test_contract.get_all_beneficiary()), 0)

        self.test_contract.add_beneficiary('mock beneficiary')
        self.test_contract.add_beneficiary('mock beneficiary 2')
        self.test_contract.add_beneficiary('mock beneficiary 3')
        self.assertEqual(len(self.test_contract.get_all_beneficiary()), 3)
        self.test_contract.delete_beneficiary(1)
        self.assertEqual(len(self.test_contract.get_all_beneficiary()), 2)
        self.assertEqual(self.test_contract.get_beneficiary(0), 'mock beneficiary')
        self.assertEqual(self.test_contract.get_beneficiary(1), 'mock beneficiary 3')
        self.assertEqual(self.test_contract.get_beneficiary(2), 'There is no such beneficiary')

if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    # python -m unittest discover -s test -p "*_test.py"
    # https://stackoverflow.com/questions/11241781/python-unittests-in-jenkins
