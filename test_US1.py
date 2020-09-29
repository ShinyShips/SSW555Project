import unittest

from gedCom_read import checkValidDates
from var import e

root_child_elements = e.root_child_elements




class TestDate(unittest.TestCase):

    def test_correct_birth_date(self):
        self.assertTrue(checkValidDates(root_child_elements[1]))

    def test_wrong_birth_date(self):
        self.assertFalse(checkValidDates(root_child_elements[2]))

    def test_correct_death_date(self):
        self.assertTrue(checkValidDates(root_child_elements[3]))

    def test_wrong_death_date(self):
        self.assertTrue(checkValidDates(root_child_elements[6]))

    def test_wrong_both_dates(self):
        self.assertFalse(checkValidDates(root_child_elements[10]))



if __name__ == '__main__':
    unittest.main()
