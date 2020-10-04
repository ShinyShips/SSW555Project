import sys, re

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from prettytable import PrettyTable

root_child_elements = []


# Path to .ged 
file_path = 'windsor-family-Andy-Nguyen.ged'

# Initialize parser/Pretty Table
gedcom_parser = Parser()


# Parse file
gedcom_parser.parse_file(file_path)

class e(object):
        root_child_elements = gedcom_parser.get_root_child_elements()
