def order_by_age (individuals):
    individuals.sort(key = lambda x: x[1])
    print(individuals)
    return 1
i = [("Connor Smith", 21), ("John Smith", 35), ("Jane Smith", 20)]
i2 = [("Connor Smith", 20), ("John Smith", 80), ("Jane Smith", 20)]
i3 = [("Connor Smith", 81), ("John Smith", 5), ("Jane Smith", 100)]
i4 = [("Connor Smith", 81), ("John Smith", 32), ("Jane Smith", 29)]
i5 = [("Connor Smith", 17), ("John Smith", 15), ("Jane Smith", 13)]