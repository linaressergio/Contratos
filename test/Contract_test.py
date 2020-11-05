import unittest

from service.contract import Contract


class ContractTestCase(unittest.TestCase):
    def setUp(self):
        self.test_contract = Contract('123', '10', 'COLSANITAS', 'ACTIVO', 'Perez', 'Pablo', '147852')

    def test_validate_contract(self):
        self.assertEqual(self.test_contract.validate_contract(self.test_contract,123),true)
        

if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    # python -m unittest discover -s test -p "*_test.py"
    # https://stackoverflow.com/questions/11241781/python-unittests-in-jenkins
