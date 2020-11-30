myfamily = {
  1: {
    "name": "Dom Ortiz",
    "age": 30,
    "marriage": "12 Apr 2020"
  },
  2: {
    "name": "Jadon Ortiz",
    'age': 36,
    "marriage": "12 Apr 2010"
  },
  3: {
    "name": "Vi Ortiz",
    "age": 35,
    "marriage": ""
  }
}


def living_single(family):
    singles = []
    for x in family:
        if (family[x]['age'] >= 30) and family[x]['marriage'] == '':
            singles.append(family[x]['name'])
    return str(singles)
