import sys, re

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from prettytable import PrettyTable
from var import e

root_child_elements = []


def generateChildElements():
    global root_child_elements
    root_child_elements = e.root_child_elements

def checkValidDates(element):
                print(element)
                # Unpack the name tuple
                (first, last) = element.get_name()
                print(str(first) + " " + str(last))
                (birthData) = element.get_birth_data()
                (deathInfo) = element.get_death_data()
                bYear  = birthData[0].split()
                if(deathInfo[2]):
                    deathYear = deathInfo[0].split()
                    if (int(deathYear[2]) > 2020):
                        print("Death Date Invalid")
                        return False
                else:
                    if (int(bYear[2]) > 2020):
                        print("Birth Date Invalid")
                        return False
                print("Birth and Death dates are valid")
                return True


def parse(allElements):
    tree = {}
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
parse(root_child_elements)
print("Type stop to end program")

while(output!= "stop"):
    output = input()
    print("-->"+output)
    print(formatOutput(output))
