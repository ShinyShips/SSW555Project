def individual_ages (names, birthdays):
    bdays = birthdays.split(" ")
    byears = bdays[2::3]
    ages = []
    for x in byears:
        age = 2020 - int(x)
        if age < 0:
            return -1
        ages.append(age)
    output = []
    for a, b in zip(names, ages):
        c = str(a) + " AGE: " + str(b)
        output.append(c)
    print(output)
    return 1

n = ["Connor Smith", "John Smith", "Jason Smith"]
bdays = ("08 APR 1999 19 JUN 1997 11 AUG 2003")
n2 = ["Connor Smith", "John Smith", "Jason Smith"]
bdays2 = ("08 APR 1999 19 JUN 1997 11 AUG 2033")
n3 = ["Connor Smith", "John Smith", "Jason Smith"]
bdays3 = ("08 APR 1999 19 JUN 1999 11 AUG 2003")
n4 = ["Connor Smith", "John Smith", "Jason Smith"]
bdays4 = ("08 APR 1999 19 JUN 1897 11 AUG 2003")
n5 = ["Connor Smith", "John Smith", "Jason Smith"]
bdays5 = ("08 APR 1999 19 JUN 1997 11 AUG 2103")
