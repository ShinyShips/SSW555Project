import sys, re, datetime

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

def checkValidDates(element):
    (birthData) = element.get_birth_data()
    (deathInfo) = element.get_death_data()
    bYear  = birthData[0].split()
    if(deathInfo[2]):
        deathYear = deathInfo[0].split()
        if (int(deathYear[2]) > 2020):
            print("ERROR: Death Date Invalid")
            return False
        else:
            if (int(bYear[2]) > 2020):
                print("ERROR: Birth Date Invalid")
                return False
    print("Birth and Death dates are valid")
    return True

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
parse(root_child_elements)
print("Type stop to end program")

while(output!= "stop"):
    output = input()
    print("-->"+output)
    print(formatOutput(output))
