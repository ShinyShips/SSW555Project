"""birth dates of siblings should be more than 8 months apart of less than 2 days"""
import math


def sibling_spacing(sibling1_birth, sibling2_birth):
    sibling1_info = sibling1_birth.split(" ")
    sibling1_year = int(sibling1_info[2])
    sibling1_month = sibling1_info[1]
    sibling1_day = int(sibling1_info[0])
    sibling2_info = sibling2_birth.split(" ")
    sibling2_year = int(sibling2_info[2])
    sibling2e_month = sibling2_info[1]
    sibling2e_day = int(sibling2_info[0])

    if sibling1_year == sibling2_year and (abs(sibling1_month - sibling2e_month) < 8):
        return -1
    elif sibling1_year == sibling2_year and (abs(sibling1_month - sibling2e_month) > 8):
        return 0
    elif sibling1_year == sibling2_year and sibling1_month == sibling2e_month and (abs(sibling1_day - sibling2e_day) > 2):
        return -1
    elif sibling1_year == sibling2_year and sibling1_month == sibling2e_month and (abs(sibling1_day - sibling2e_day) < 2):
        return 0
    else:
        return 1


def numerical_month(month):
    return{'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
           'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}[month]