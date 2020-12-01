def upcoming_anniversaries(a):
    a = a.split(" ")
    day = int(a[0])
    month = a[1]
    year = a[2]
    if year == "2020":
        if month == "NOV":
            if day >= 30:
                return 1
        if month == "DEC":
            return 1
        else:
            return -1
    else:
        return -1
a1 = "12 DEC 2020"
a2 = "31 NOV 2020"
a3 = "12 AUG 2020"
a4 = "12 AUG 1935"
a5 = "21 DEC 2020"