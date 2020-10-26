from collections import Counter
"""NO more than 5 children born on the same day"""


def multiple_births(element):
    children = element.get_child_elements()
    if len(children) < 6:
        return 0
    else:
        birth_dates = []
        for c in children:
            birth_dates.append(c.get_birth_data)
        for b in birth_dates:
            if birth_dates.count(b) > 5:
                return 1
            else:
                return 0
