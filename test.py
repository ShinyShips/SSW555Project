import unittest
from US06 import divorce_before_death
from US05 import marriage_before_death
from US13 import sibling_spacing


class TestStories(unittest.TestCase):

    def test_divorceBeforeDeath(self):
        self.assertEqual(divorce_before_death("24 JAN 1998", "24 JAN 1990"), 'divorced before death')
        self.assertEqual(divorce_before_death(" ", "24 JAN 1998"), 'not dead')
        self.assertEqual(divorce_before_death("24 JAN 1998", " "), 'never divorced')
        self.assertEqual(divorce_before_death("24 JAN 1998", "24 JAN 2000"),  'not divorced before death')
        self.assertEqual(divorce_before_death("24 JAN 1998", "23 JAN 1998"),  'divorced before death')

    def test_marriageBeforeDeath(self):
        self.assertEqual(marriage_before_death("24 JAN 1998", "24 JAN 1990"), 'married before death')
        self.assertEqual(marriage_before_death(" ", "24 JAN 1998"), 'not dead')
        self.assertEqual(marriage_before_death("24 JAN 1998", " "), 'never married')
        self.assertEqual(marriage_before_death("24 JAN 1998", "24 JAN 2000"),  'not married before death')
        self.assertEqual(marriage_before_death("24 JAN 1998", "23 JAN 1998"),  'married before death')

    def sibling_spacing(self):
        self.assertEqual(sibling_spacing("24 JAN 1998", "25 JAN 1990"), 0)
        self.assertEqual(sibling_spacing("24 JAN 1998", "24 FEB 1990"), -1)


if __name__ == '__main__':
    unittest.main()


