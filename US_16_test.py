import unittest
from US_16 import checklastnames

class MyTestCase(unittest.TestCase):
    def test_checklastnames(self):
        self.assertEqual(checklastnames("Connor Smith", ("Jim Smith", "Joe Smith")), 1)
        self.assertEqual(checklastnames("Connor Beckham", ("Jim Beckham", "Joe Beckham", "Jane Beckham", "David Beckham")), 1)
        self.assertEqual(checklastnames("Connor Smith", ("Jim Smith", "Jason Alexander")), -1)
        self.assertEqual(checklastnames("Connor Smith", ("Jim Smith", "Smith Joe")), -1)
        self.assertEqual(checklastnames("Connor Smith", ("Jim Smith", "Joe Smit")), -1)

if __name__ == '__main__':
    unittest.main()
