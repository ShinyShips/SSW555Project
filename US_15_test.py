import unittest
from US_15 import check15siblings
from US_15 import t1,t2,t3,t4,t5

class FunctionTestCase(unittest.TestCase):
    def testcheck15siblings(self):
        self.assertEqual(check15siblings(t1), -1)
        self.assertEqual(check15siblings(t2), -1)
        self.assertEqual(check15siblings(t3), 1)
        self.assertEqual(check15siblings(t4), 1)
        self.assertEqual(check15siblings(t5), 1)

if __name__ == '__main__':
    unittest.main()
