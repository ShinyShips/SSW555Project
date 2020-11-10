from US_27 import individual_ages
from US_27 import n, n2, n3, n4, n5, bdays, bdays2, bdays3, bdays4, bdays5
import unittest

class MyTestCase(unittest.TestCase):
    def test_individual_ages(self):
        self.assertEqual(individual_ages(n,bdays), 1)
        self.assertEqual(individual_ages(n2, bdays2), -1)
        self.assertEqual(individual_ages(n3, bdays3), 1)
        self.assertEqual(individual_ages(n4, bdays4), 1)
        self.assertEqual(individual_ages(n5, bdays5), -1)

if __name__ == '__main__':
    unittest.main()
