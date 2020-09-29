import sys, re
#checks if birth is before death
def birthBeforeDeath(death_date,birth_date):
    deathInfo = death_date.split(" ");
    if(len(deathInfo) < 3):
        return -1
    dYear = int(deathInfo[2])
    dMonth = deathInfo[1]
    dDay = int(deathInfo[0])
    birthInfo = birth_date.split(" ");
    if(len(birthInfo) < 3):
        return -1
    bYear = int(birthInfo[2])
    bMonth = birthInfo[1]
    bDay = int(birthInfo[0])
    if(bYear < dYear):
        return 1
    elif(bYear == dYear):
        if(turnMonthToNum(dMonth) > turnMonthToNum(bMonth)):
           return 1
        elif(turnMonthToNum(dMonth) == turnMonthToNum(bMonth)):
            if(dDay > bDay):
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

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

    
