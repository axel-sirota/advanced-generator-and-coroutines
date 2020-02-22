def pipeline(number):
    data = (i for i in range(number))
    squared = (i**2 for i in data)
    negated = (-i for i in squared)
    return (n + d + 1 for n in negated for d in data)


