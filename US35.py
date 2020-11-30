def recent_births(family):
    recent = []

    for x in family:
        birthday = family[x]['bday']
        byear = birthday[7:11]
        bmonth = birthday[3:6]
        bdate = birthday[0:2]
        if byear == '2020' and bmonth == 'Nov':
            recent.append(family[x]['name'])
    return str(recent)


myfamily = {
  1: {
    "name": "Dom Ortiz",
    "bday": '24 Jan 1998',
  },
  2: {
    "name": "Jadon Ortiz",
    'bday': '15 Nov 2002',
  },
  3: {
    "name": "Vi Ortiz",
    "bday": '01 Nov 2020',
  }
}

