import unittest

#Andy Scipts
#from gedCom_read import checkValidDates
#from gedCom_read import checkBirthBeforeDeathOfParents
#from gedCom_read import checkMarriageAfter14
from var import e
root_child_elements = e.root_child_elements

#Kyle Scripts
import birthBeforeDeath
import marriageBeforeDivorce

#Connor Scripts
import SSW555_US7
import US_08
import US_15
import US_16

#Dom Scripts
import US05
import US06
import US13

class TestUserStory(unittest.TestCase):

    def test_correct_birth_date(self):
        self.assertTrue(checkValidDates(root_child_elements[1]))

    def test_wrong_birth_date(self):
        self.assertTrue(checkValidDates(root_child_elements[2]))

    def test_correct_death_date(self):
        self.assertTrue(checkValidDates(root_child_elements[3]))

    def test_wrong_death_date(self):
        self.assertTrue(checkValidDates(root_child_elements[6]))

    def test_wrong_both_dates(self):
        self.assertTrue(checkValidDates(root_child_elements[10]))

    def test_family_head(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[9]))

    def test_family_head_spouse(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[11]))

    def test_first_child(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[3]))

    def test_grand_child(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[6]))

    def test_great_grand_child(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[10]))

    def test_family_head1(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[1]))

    def test_family_head_spouse1(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[2]))

    def test_first_child1(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[3]))

    def test_grand_child1(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[6]))

    def test_great_grand_child1(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[10]))
    

    def test_birthBeforeDeath(self):
        tester = birthBeforeDeath
        self.assertEqual(tester.birthBeforeDeath("9 APR 1999","8 APR 1999"), 1)
        self.assertEqual(tester.birthBeforeDeath("3 APR 1920","5 APR 2010"), -1)
        self.assertEqual(tester.birthBeforeDeath("12 JAN 1999","10 JAN 1999"), 1)
        self.assertEqual(tester.birthBeforeDeath("20 APR 2010","8 APR"), -1)
        self.assertEqual(tester.birthBeforeDeath("10 FEB 2000","8 APR 1999"), 1)
        
    def test_marriageBeforeDivorce(self):
        tester = marriageBeforeDivorce
        self.assertEqual(tester.marriageBeforeDivorce("20 APR 2010","8 APR 1999"), -1)
        self.assertEqual(tester.marriageBeforeDivorce("30 MAY 2009","26 FEB 1999"), -1)
        self.assertEqual(tester.marriageBeforeDivorce("1 JAN 2000","2 JAN 2000"), 1)
        self.assertEqual(tester.marriageBeforeDivorce("3 OCT 2007","26 OCT 2007"), 1)
        self.assertEqual(tester.marriageBeforeDivorce("4 DEC 2010","3 DEC 2010"), -1)

    def test_check_age(self):
        tester = SSW555_US7
        self.assertEqual((tester.check_age("8 DEC 2019", "21 AUG 1999")), 1)
        self.assertEqual((tester.check_age("11 MAR 3019", "1 SEP 1999")), 0)
        self.assertEqual((tester.check_age("30 APR 2013", "12 DEC 1699")), 0)
        self.assertEqual((tester.check_age("NA", "17 FEB 1899")), 1)
        self.assertEqual((tester.check_age("NA", "18 JAN 1999")), 1)

    def test_check_child(self):
        tester = US_08
        self.assertEqual(tester.check_child("8 APR 1999", "04 MAR 1994", "12 JUN 2003"), 1)
        self.assertEqual(tester.check_child("8 APR 1999", "04 MAR 1994", "NA"), 1)
        self.assertEqual(tester.check_child("8 APR 1998", "04 MAR 1994", "12 JUN 2003"), 1)
        self.assertEqual(tester.check_child("8 APR 1999", "04 MAR 1994", "12 JUN 2003"), 1)
        self.assertEqual(tester.check_child("8 APR 2003", "04 MAR 1999", "12 JUN 2001"), -1)

    def test_marriage_before_death(self):
        tester = US05
        self.assertEqual(tester.marriage_before_death("24 JAN 1998", "24 JAN 1990"), 'married before death')
        self.assertEqual(tester.marriage_before_death(" ", "24 JAN 1998"), 'not dead')
        self.assertEqual(tester.marriage_before_death("24 JAN 1998", " "), 'never married')
        self.assertEqual(tester.marriage_before_death("24 JAN 1998", "24 JAN 2000"), 'not married before death')
        self.assertEqual(tester.marriage_before_death("24 JAN 1998", "23 JAN 1998"), 'married before death')
        
        
    def test_divorce_before_death(self):
        tester = US06
        self.assertEqual(tester.divorce_before_death("24 JAN 1998", "24 JAN 1990"), 'divorced before death')
        self.assertEqual(tester.divorce_before_death(" ", "24 JAN 1998"), 'not dead')
        self.assertEqual(tester.divorce_before_death("24 JAN 1998", " "), 'never divorced')
        self.assertEqual(tester.divorce_before_death("24 JAN 1998", "24 JAN 2000"), 'not divorced before death')
        self.assertEqual(tester.divorce_before_death("24 JAN 1998", "23 JAN 1998"), 'divorced before death')
        

    def sibling_spacing(self):
        self.assertEqual(tester.sibling_spacing("24 JAN 1998", "25 JAN 1990"), 0)
        self.assertEqual(tester.sibling_spacing("24 JAN 1998", "24 FEB 1990"), -1)

if __name__ == '__main__':
    unittest.main()
