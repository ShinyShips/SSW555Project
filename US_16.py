def checklastnames(e, men):
    e1 = e.split(' ')
    e2 = e1[1]
    mens = str(men)
    men2 = mens.split(' ')
    men_surname = men2[1::2]
    surnames = list()
    substring = e2
    for name in men_surname:
        if substring in name:
            surnames.append(substring)
        else:

            return -1

    return 1