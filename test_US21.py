import unittest

from gedCom_read import correctGenderForRole
from var import e

root_child_elements = e.root_child_elements




class TestDate(unittest.TestCase):

    def test_family_head(self):
        self.assertTrue(correctGenderForRole(root_child_elements[1]))

    def test_family_head_spouse(self):
        self.assertTrue(correctGenderForRole(root_child_elements[2]))

    def test_first_child(self):
        self.assertTrue(correctGenderForRole(root_child_elements[3]))

    def test_grand_child(self):
        self.assertTrue(correctGenderForRole(root_child_elements[6]))

    def test_great_grand_child(self):
        self.assertTrue(correctGenderForRole(root_child_elements[10]))



if __name__ == '__main__':
    unittest.main()
