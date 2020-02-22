from collections import Iterable


def delegating_without_yield():
    for c in ['Hello', 'Pluralsighters']:
        yield c


def delegating_with_yield():
    yield from ['Hello', 'Pluralsighters']


def chain(*iterables):
    for it in iterables:
        yield from it


# Python Cookbook courtesy
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
