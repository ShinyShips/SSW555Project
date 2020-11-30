import unittest
from US31 import living_single
from US31 import myfamily


class MyTestCase(unittest.TestCase):
    def test_living_single(self):
        self.assertEqual(living_single(myfamily), "['Vi Ortiz']")


if __name__ == '__main__':
    unittest.main()