from datetime import date, timedelta

current_date = date.today().isoformat()   
days_after = (date.today()+timedelta(days=30)).isoformat()
limit_day = days_after[8:10]
limit_month = days_after[5:7]
limit_year = days_after[0:4]

def upcoming_birthdays(family):
    upcoming = []

    for x in family:
        birthday = family[x]['bday']
        byear = birthday[7:11]
        bmonth = birthday[3:6]
        bdate = birthday[0:2]
        if int(byear) <= int(limit_year) and turnMonthToNum(bmonth) == int(limit_month):
            upcoming.append(family[x]['name'])
    return str(upcoming)

myfamily = {
  1: {
    "name": "Dom Ortiz",
    "bday": '24 DEC 2020',
  },
  2: {
    "name": "Jadon Ortiz",
    'bday': '15 NOV 2002',
  },
  3: {
    "name": "Vi Ortiz",
    "bday": '01 NOV 2020',
  }
}

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
