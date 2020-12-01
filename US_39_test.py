import unittest
from US_39 import upcoming_anniversaries, a1,a2,a3,a4,a5

class MyTestCase(unittest.TestCase):
    def test_upcoming_anniversaries(self):
        self.assertEqual(upcoming_anniversaries(a1), 1)
        self.assertEqual(upcoming_anniversaries(a2), 1)
        self.assertEqual(upcoming_anniversaries(a3), -1)
        self.assertEqual(upcoming_anniversaries(a4), -1)
        self.assertEqual(upcoming_anniversaries(a5), 1)

if __name__ == '__main__':
    unittest.main()
