import sys, re

from datetime import datetime

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from prettytable import PrettyTable
from var import e

root_child_elements = []
# Path to .ged 
file_path = 'windsor-family-Andy-Nguyen.ged'

# Initialize parser/Pretty Table
gedcom_parser = Parser()


# Parse file
gedcom_parser.parse_file(file_path)


def generateChildElements():
    global root_child_elements
    root_child_elements = e.root_child_elements

# US01
def checkValidDates(individual):
    (birthData) = individual.get_birth_data()
    (deathData) = individual.get_death_data()
    if(deathData[2]):
        birthDate = birthData[0].split()
        deathDate = deathData[0].split()
        birthYear = int(birthDate[2])
        deathYear = int(deathDate[2])
        if (deathYear > 2020):
            print("ERROR: Death Date Invalid")
            return False
        else:
            if (birthYear > 2020):
                print("ERROR: Birth Date Invalid")
                return False
    print("Birth and Death dates are valid")
    return True

# US02
def checkBirthBeforeMarriage(individual):
    marriages = gedcom_parser.get_marriage_years(individual)
    (birthData) = individual.get_birth_data()
    
def checkForBigamy(element):
    marriages = gedcom_parser.get_marriage_years(element)
    divorces = gedcom_parser.get_divorce_years(element)
    numMarriages = len(marriages)
    numDivorce = len(divorces)
    counter = 0;
    
    if(numMarriages > numDivorce+1):
        print("Too many marriages compared to divorces")
        return False
    
    #makes sure divorce dates are before corresponding marriage dates.
    for i in range(numMarriages):
        for j in range(i,numDivorce):
            if(checkDates(divorces[j],marriages[i]) == -1):
                print("Divorce date is before marriage date")
                return False

    if(numMarriages>1):
        for k in range(numMarriages-1):
            if(checkDates(marriages[k+1],marriages[k]) == -1):
                print("Marriage #"+(k+1)+" is before Marriage #"+k)
                return False
    return True
                
def checkBirthBeforeMarriage(element):
    marriages = gedcom_parser.get_marriage_years(element)
    (birthData) = element.get_birth_data()
    bDate = birthData[0].split()
    bYear = int(bDate[2])
    numMarriages  = len(marriages)
    counter = 0
    
    if marriages:
        while counter < numMarriages:
            weddingYear = marriages[counter]
            if  bYear > weddingYear:
                print ("ERROR: Birth is after Marriage")
                return False
            counter += 1
    print ("Birth is before Marriage")
    return True

# US09
def checkBirthBeforeDeathOfParents(individual):
        checkFather = False
        checkMother = False
        parents = gedcom_parser.get_parents(individual)

        childBirthDate = getBirthDay(individual)
        if (parents):
            fatherDeathDate = getDeathDay(parents[0])
            motherDeathDate = getDeathDay(parents[1])
        else:
            return True

        if (fatherDeathDate == None):
            checkFather = True 
        elif (monthsBetween(fatherDeathDate, childBirthDate) > 9):
            checkFather = True
        else:
            checkFather = False

        if (motherDeathDate == None):
            checkMother = True 
        elif (monthsBetween(motherDeathDate, childBirthDate) <= 0):
            checkMother = True
        else:
            checkMother = False

        if (checkFather and checkMother):
            print ("Born in valid dates")
            return True
        else:
            print ("Not born in valid dates")
            return False


# US10
def checkMarriageAfter14(individual):
        marriages = gedcom_parser.get_marriages(individual)
        marriage_dates = [idx for idx, val in marriages]
        marriage_datetimes = []
        for date in marriage_dates:
            marriage_datetimes.append(convertDateListToDateTime(date.split()))

        for datetime in marriage_datetimes:
            print(getBirthDay(individual))
            print(datetime)
            print (yearsBetween(getBirthDay(individual), datetime))
            if (yearsBetween(getBirthDay(individual), datetime) < 14):
                return False

        families = gedcom_parser.get_families(individual)

        index = 0

        while index < len(families):
            members = gedcom_parser.get_family_members(families[index])
            spouse = members[1]
            spouseBirthday = getBirthDay(spouse)
            print(yearsBetween(spouseBirthday, marriage_datetimes[index]))
            if (yearsBetween(spouseBirthday, marriage_datetimes[index]) < 14):
                return False
            index += 1
        return True

# Helper Functions
def convertDateListToDateTime(list):
    if (list[1] == 'JAN'):
        month = 1
    elif (list[1] == 'FEB'):
        month = 2
    elif (list[1] == 'MAR'):
        month = 3
    elif (list[1] == 'APR'):
        month = 4
    elif (list[1] == 'MAY'):
        month = 5
    elif (list[1] == 'JUN'):
        month = 6
    elif (list[1] == 'JUL'):
        month = 7
    elif (list[1] == 'AUG'):
        month = 8
    elif (list[1] == 'SEP'):
        month = 9
    elif (list[1] == 'OCT'):
        month = 10
    elif (list[1] == 'NOV'):
        month = 11
    elif (list[1] == 'DEC'):
        month = 12
    
    day = int(list[0])
    year = int(list[2])

    d = datetime(year, month, day)
    return d

def getBirthDay(individual):
    (birthData) = individual.get_birth_data()
    bDate = birthData[0].split()
    bDate = convertDateListToDateTime(bDate)
    return bDate

def getDeathDay(individual):
    (deathData) = individual.get_death_data()
    if (deathData[0] == ''):
        return None
    dDate = deathData[0].split()
    dDate = convertDateListToDateTime(dDate)
    return dDate

def monthsBetween(parent, child):
    num_months = (child.year - parent.year) * 12 + (child.month - parent.month)
    return num_months

def yearsBetween(birth, marriage):
    num_years = (marriage.year - birth.year)
    return num_years
def checkDates(later,early):
    if(early[2] < later[2]):
        return 1
    elif(early[2] == later[2]): 
        if(turnMonthToNum(later[1]) > turnMonthToNum(early[1])):
            return 1
        elif(turnMonthToNum(later[1]) == turnMonthToNum(early[1])):
            if(later[0] > early[0]):
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

def dateChecker(later_date,early_date):
    #formats data
    later_info = later_date.split(" ");
    early_info = early_date.split(" ");
    if(len(later_info) < 3):
        return -1
    if(len(early_info) < 3):
        return -1
    #year
    later_info[2] = int(later_info[2]);
    early_info[2] = int(early_info[2]);
    #day
    later_info[0] = int(later_info[0]);
    early_info[0] = int(early_info[0]);
    #month is kept the same because we working with string
    if(checkDates(later_info,early_info) == 1):
        return 1
    else:
        return -1

def turnMonthToNum(month):
    return{
        'JAN' : 1,
        'FEB' : 2,
        'MAR' : 3,
        'APR' : 4,
        'MAY' : 5,
        'JUN' : 6,
        'JUL' : 7,
        'AUG' : 8,
        'SEP' : 9, 
        'OCT' : 10,
        'NOV' : 11,
        'DEC' : 12
    }[month]

def parse(allElements):
    # tree = {}
    generateChildElements()
    IndividualTable = PrettyTable()
    FamilyTable = PrettyTable()
    # Iterate through elements
    for element in root_child_elements:
        if isinstance(element, IndividualElement):
               # print(gedcom_parser.get_families(element,"gedcom.tags.GEDCOM_TAG_FAMILY_SPOUSE"))
                # Unpack the name tuple
                (first, last) = element.get_name()
                (gender) = element.get_gender()
                (birthData) = element.get_birth_data()
                (deathInfo) = element.get_death_data()
                (ID) = element.get_pointer()
                bYear  = birthData[0].split()
                if(deathInfo[2]):
                    deathYear = deathInfo[0].split()
                    age = int(deathYear[2]) - int(bYear[2])
                    alive = 0
                    death = deathInfo[0]
                else:
                    age = 2020 - int(bYear[2])
                    alive = 1
                    death = "NA"
                
                
                #input information into pretty table
                IndividualTable.field_names = ["ID","First","Last","Gender","Age", "Alive", "Death"]
                IndividualTable.add_row([ID.strip("@"),first,last,gender,age,bool(alive),death])

    print("Individual Table")
    print(IndividualTable)
    print("Family Table")
    print(FamilyTable)

def formatOutput(line):
    output =  line.split()
    output.insert(1,"|")
    output.insert(3,"|")
    checker = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRTL","NOTE"]
    if output[2] in checker:
        output.insert(4,"Y")
    else:
        output.insert(4,"N")
    output.insert(5,"|")
    fOutput = " ".join(output)
    return "<--" +fOutput

output =""
generateChildElements()
checkValidDates(root_child_elements[1])
checkBirthBeforeMarriage(root_child_elements[1])
checkBirthBeforeDeathOfParents(root_child_elements[8])
checkMarriageAfter14(root_child_elements[1])
parse(root_child_elements)
print("Type stop to end program")

while(output!= "stop"):
    output = input()
    print("-->"+output)
    print(formatOutput(output))
