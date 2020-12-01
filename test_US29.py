import unittest

from gedCom_read import listDeceased
from var import e

root_child_elements = e.root_child_elements




class TestDate(unittest.TestCase):

    def test_family_head(self):
        self.assertFalse(listDeceased(root_child_elements, root_child_elements[1]))

    def test_family_head_spouse(self):
        self.assertFalse(listDeceased(root_child_elements, root_child_elements[2]))

    def test_dead_family_member(self):
        self.assertTrue(listDeceased(root_child_elements, root_child_elements[5]))

    def test_grand_child(self):
        self.assertFalse(listDeceased(root_child_elements, root_child_elements[6]))

    def test_great_grand_child(self):
        self.assertFalse(listDeceased(root_child_elements, root_child_elements[10]))



if __name__ == '__main__':
    unittest.main()
