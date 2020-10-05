# Connor Smith
# SSW 555 HW$
def check_age(death_date, birth_date):
    if death_date != "NA":
        death_year = death_date.split(" ")
        birth_year = birth_date.split(" ")
        age = int(death_year[2]) - int(birth_year[2])
        if age >= 150:
            return 0
        else:
            return 1
    else:
        birth_year = birth_date.split(" ")
        age = 2020 - int(birth_year[2])
        if age >= 150:
            return 0
        else:
            return 1



