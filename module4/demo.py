from numpy import random, mean
from collections import namedtuple

from module4 import coroutine


@coroutine
def averager_with_result_and_exceptions():
    print('-> coroutine started')
    Result = namedtuple('Result', ['Count', 'Average'])
    total = 0
    sum_up_to_now = 0
    average = None
    while True:
        try:
            value = yield average
        except ValueError:
            print('*** ValueError handled. Continuing...')
        except GeneratorExit:
            print(f'This is executed if I get closed, so I need to cleanup here and die gracefully. \nMy intermediate '
                  f'result is {Result(total, average)}')
            raise
        else:
            if value is None:
                break
            total += 1
            sum_up_to_now += value
            average = sum_up_to_now / total
    return Result(total, average)


def main(size):
    averager = averager_with_result_and_exceptions()
    magic_values = random.randint(0, 25, size=size)
    print(f'Real average: {mean(magic_values)}')
    try:
        for value in magic_values:
            averager.send(value)
            if value == 1:
                averager.throw(ValueError)
            if value == 3:
                averager.close()
        next(averager)
    except StopIteration as exc:
        returned_value = exc.value
        print(f'Final result: {returned_value}')
    except GeneratorExit:
        pass


if __name__ == '__main__':
    main(40)
