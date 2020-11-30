import unittest
from US35 import recent_births
from US35 import myfamily


class MyTestCase(unittest.TestCase):
    def test_recent_birth(self):
        self.assertEqual(recent_births(myfamily), "['Vi Ortiz']")


if __name__ == '__main__':
    unittest.main()