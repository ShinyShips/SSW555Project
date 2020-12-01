import unittest
from US_42 import check_real_dates, d1,d2,d3,d4,d5

class MyTestCase(unittest.TestCase):
    def test_check_real_dates(self):
        self.assertEqual(check_real_dates(d1), 1)
        self.assertEqual(check_real_dates(d2), -1)
        self.assertEqual(check_real_dates(d3), -1)
        self.assertEqual(check_real_dates(d4), -1)
        self.assertEqual(check_real_dates(d5), 1)

if __name__ == '__main__':
    unittest.main()
