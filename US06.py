import sys,re
#dominic ortiz


def divorce_before_death(death_date, divorce_date):
    death_info = death_date.split(" ")
    if len(death_info) < 3:
        return 'not dead'
    death_year = int(death_info[2])
    death_month = death_info[1]
    death_day = int(death_info[0])
    divorce_info = divorce_date.split(" ")
    if len(divorce_info) < 3:
        return 'never divorced'
    divorce_year = int(divorce_info[2])
    divorce_month = divorce_info[1]
    divorce_day = int(divorce_info[0])
    if divorce_year < death_year:
        return 'divorced before death'
    elif divorce_year == death_year:
        if numerical_month(death_month) > numerical_month(divorce_month):
            return 'divorced before death'
        elif numerical_month(death_month) == numerical_month(divorce_month):
            if death_day > divorce_day:
                return 'divorced before death'
            else:
                return 'not divorced before death'
        else:
            return 'not divorced before death'
    else:
        return 'not divorced before death'



def numerical_month(month):
    return{'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
           'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}[month]


