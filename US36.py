def recent_deaths(family):
    recent = []

    for x in family:
        dday = family[x]['dday']
        dyear = dday[7:11]
        dmonth = dday[3:6]
        ddate = dday[0:2]
        if dyear == '2020' and turnMonthToNum(dmonth) >= turnMonthToNum('NOV'):
            recent.append(family[x]['name'])
    return str(recent)


myfamily = {
  1: {
    "name": "Dom Ortiz",
    "dday": '24 JAN 1998',
  },
  2: {
    "name": "Jadon Ortiz",
    'dday': '15 NOV 2002',
  },
  3: {
    "name": "Vi Ortiz",
    "dday": '01 NOV 2020',
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

