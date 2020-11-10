import unittest

#Andy Scipts
from gedCom_read import checkValidDates
from gedCom_read import checkBirthBeforeDeathOfParents
from gedCom_read import checkMarriageAfter14
from gedCom_read import checkSiblingsNotMarried
from gedCom_read import correctGenderForRole
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
from US_27 import individual_ages
from US_27 import n, n2, n3, n4, n5, bdays, bdays2, bdays3, bdays4, bdays5
from US_28 import order_by_age
from US_28 import i,i2,i3,i4,i5


#Dom Scripts
import US05
import US06
import US13

class TestUserStory(unittest.TestCase):

    def test_checkValidDates(self):
        self.assertTrue(checkValidDates(root_child_elements[1]))
        self.assertTrue(checkValidDates(root_child_elements[2]))
        self.assertTrue(checkValidDates(root_child_elements[3]))
        self.assertTrue(checkValidDates(root_child_elements[6]))
        self.assertTrue(checkValidDates(root_child_elements[10]))

    def test_checkBirthBeforeDeathOfParents(self):
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[9]))
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[11]))
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[3]))
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[6]))
        self.assertTrue(checkBirthBeforeDeathOfParents(root_child_elements[10]))

    def test_checkMarriageAfter14(self):
        self.assertTrue(checkMarriageAfter14(root_child_elements[1]))
        self.assertTrue(checkMarriageAfter14(root_child_elements[2]))
        self.assertTrue(checkMarriageAfter14(root_child_elements[3]))
        self.assertTrue(checkMarriageAfter14(root_child_elements[6]))
        self.assertTrue(checkMarriageAfter14(root_child_elements[10]))

    def test_checkSiblingsNotMarried(self):
        self.assertTrue(checkSiblingsNotMarried(root_child_elements[1]))
        self.assertTrue(checkSiblingsNotMarried(root_child_elements[2]))
        self.assertTrue(checkSiblingsNotMarried(root_child_elements[3]))
        self.assertTrue(checkSiblingsNotMarried(root_child_elements[6]))
        self.assertTrue(checkSiblingsNotMarried(root_child_elements[10]))

    def test_correctGenderForRole(self):
        self.assertTrue(correctGenderForRole(root_child_elements[1]))
        self.assertTrue(correctGenderForRole(root_child_elements[2]))
        self.assertTrue(correctGenderForRole(root_child_elements[3]))
        self.assertTrue(correctGenderForRole(root_child_elements[6]))
        self.assertTrue(correctGenderForRole(root_child_elements[10]))
    

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

    def test_individual_ages(self):
        self.assertEqual(individual_ages(n,bdays), 1)
        self.assertEqual(individual_ages(n2, bdays2), -1)
        self.assertEqual(individual_ages(n3, bdays3), 1)
        self.assertEqual(individual_ages(n4, bdays4), 1)
        self.assertEqual(individual_ages(n5, bdays5), -1)

    def test_order_by_age(self):
        self.assertEqual(order_by_age(i), 1)
        self.assertEqual(order_by_age(i2), 1)
        self.assertEqual(order_by_age(i3), 1)
        self.assertEqual(order_by_age(i4), 1)
        self.assertEqual(order_by_age(i5), 1)
        


if __name__ == '__main__':
    unittest.main()
