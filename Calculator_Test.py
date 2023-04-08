import re
import unittest
from Tax_Calculator import progressive, standard, married_tax

class TestMessage(unittest.TestResult):
    def addSuccess(self, test):
        test_number = test._testMethodName.split('_')[-1]
        super().addSuccess(test)
        print(f"Test {test_number} passed!\n")

    def addFailure(self, test, err):
        test_number = test._testMethodName.split('_')[-1]
        super().addFailure(test, err)
        msg = str(err[1])
        actual, expected = self._parse_msg(msg)
        print(f"Test {test_number} failed! Expected: {expected}, Actual: {actual}\n")
    def _parse_msg(self, msg):
        tuple_pattern = r'\((.*?)\)'
        tuples = re.findall(tuple_pattern, msg)
        actual = tuples[0]
        expected = tuples[1]
        return actual, expected

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(married_tax(0, 350000),(0, 17500, 2110, 16085))
    def test_2(self):
        self.assertEqual(married_tax(350000, 0),(17500, 0, 2110, 16085))
    def test_3(self):
        self.assertEqual(married_tax(1400000, 150000),(70000, 7500, 196285, 194710))
    def test_4(self):
        self.assertEqual(married_tax(350000, 1200000),(17500, 60000, 194585, 176585))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(resultclass=TestMessage, verbosity=0).run(suite)