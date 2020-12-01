def check_real_dates(date):
        date = date.split(" ")
        day = int(date[0])
        month = date[1]
        year = int(date[2])
        if month == "JAN" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "FEB" and day <= 29:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "MAR" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "APR" and day <= 30:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "MAY" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "JUN" and day <= 30:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "JUL" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "AUG" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "SEP" and day <= 30:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "OCT" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "NOV" and day <= 30:
            if year <= 2020:
                return 1
            else:
                return -1
        if month == "DEC" and day <= 31:
            if year <= 2020:
                return 1
            else:
                return -1
        else:
            return -1
d1 = ("10 DEC 2000")
d2 = ("100 DEC 2000")
d3 = ("10 DEC 2030")
d4 = ("10 DECE 2000")
d5 = ("1 MAR 1935")