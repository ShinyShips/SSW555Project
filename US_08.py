def check_child(child_bday, marriage_date, divorce_date):
    birthInfo = child_bday.split(" ")
    bYear = int(birthInfo[2])
    bMonth = birthInfo[1]
    bDay = int(birthInfo[0])
    marriageInfo = marriage_date.split(" ")
    mYear = (birthInfo[2])
    mMonth = (birthInfo)[1]
    mDay = int(birthInfo[0])
    if divorce_date != "NA":
        divorce_date = divorce_date.split(" ")
        dYear = (divorce_date[2])
        dMonth = (divorce_date[1])
        dDay = int(divorce_date[0])
    else:
        pass
    if divorce_date == "NA":
        if int(bYear) >= int(mYear):
            return 1
        else:
            return -1
    else:
        if int(bYear) < int(dYear):
            return 1
        elif int(bYear) == int(dYear):
            if (turnMonthToNum(dMonth) - turnMonthToNum(bMonth)) > 9:
                return 1
            elif (turnMonthToNum(dMonth) - turnMonthToNum(bMonth)) <= 9:
                if int(dDay) > (bDay):
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1

def turnMonthToNum(month):
        return dict(JAN=1, FEB=2, MAR=3, APR=4, MAY=5, JUN=6, JUL=7, AUG=8, SEP=9, OCT=10, NOV=11, DEC=12)[month]
