from US_28 import order_by_age
from US_28 import i,i2,i3,i4,i5

import unittest

class MyTestCase(unittest.TestCase):
    def test_order_by_age(self):
        self.assertEqual(order_by_age(i), 1)
        self.assertEqual(order_by_age(i2), 1)
        self.assertEqual(order_by_age(i3), 1)
        self.assertEqual(order_by_age(i4), 1)
        self.assertEqual(order_by_age(i5), 1)

if __name__ == '__main__':
    unittest.main()
