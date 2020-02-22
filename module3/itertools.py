import itertools


def old_style_averager(iterable):
    total_sum = 0
    total_elements = 0
    average = []
    for number in iterable:
        total_sum += number
        total_elements += 1
        average.append(total_sum/total_elements)
    return average


def generator_averager(iterable):
    total_sum = 0
    total_elements = 0
    for number in iterable:
        total_sum += number
        total_elements += 1
        yield total_sum/total_elements


def averager(iterable):
    return itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(iterable), 1))

