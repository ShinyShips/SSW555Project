import sys, re
#checks if marriage date is before divorce date
def marriageBeforeDivorce(marr_date,divorce_date):
    divorceInfo = divorce_date.split(" ");
    marryInfo = marr_date.split(" ");
    if(len(marryInfo) < 3):
        return "Individual was never married"
    if(len(divorceInfo)< 3):
        return "Individual was never divorced"
    
    dYear = int(divorceInfo[2])
    dMonth = divorceInfo[1]
    dDay = int(divorceInfo[0])
    
    mYear = int(marryInfo[2])
    mMonth = marryInfo[1]
    mDay = int(marryInfo[0])
    
    if(mYear < dYear):
        return 1
    elif(mYear == dYear):
        if(turnMonthToNum(dMonth) > turnMonthToNum(mMonth)):
           return 1
        elif(turnMonthToNum(dMonth) == turnMonthToNum(mMonth)):
            if(dDay > mDay):
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

    
