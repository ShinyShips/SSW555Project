# Connor Smith
# US08
def checkBirthBeforeMarriageParents(element):
    (birthData) = element.get_birth_data()
    birthDate = birthData[0]
    parents = element.get_parents()
    marriage_date = parents.get_marriage[0]
    marriage_years = parents.get_marriage_years()
    divorce_year = parents.get_marriage_years[-1]
    if int(birthDate) <= int(marriage_date):
        print("Error this child was born before marriage")
        return 0
        if int(birthDate[0]) > int(divorce_year):
            print("Error this child was born after divorce")
            return 0
        else:
            print("birth is weird but still ok")
            retrun
            1
    else:
        print("birth is ok")
        return 1

