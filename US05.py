import sys,re
#dominic Ortiz


def marriage_before_death(death_date, marriage_date):
    death_info = death_date.split(" ")
    if len(death_info) < 3:
        return 'not dead'
    death_year = int(death_info[2])
    death_month = death_info[1]
    death_day = int(death_info[0])
    marriage_info = marriage_date.split(" ")
    if len(marriage_info) < 3:
        return 'never married'
    marriage_year = int(marriage_info[2])
    marriage_month = marriage_info[1]
    marriage_day = int(marriage_info[0])
    if marriage_year < death_year:
        return 'married before death'
    elif marriage_year == death_year:
        if numerical_month(death_month) > numerical_month(marriage_month):
            return 'married before death'
        elif numerical_month(death_month) == numerical_month(marriage_month):
            if death_day > marriage_day:
                return 'married before death'
            else:
                return 'not married before death'
        else:
            return 'not married before death'
    else:
        return 'not married before death'


def numerical_month(month):
    return{'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
           'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}[month]