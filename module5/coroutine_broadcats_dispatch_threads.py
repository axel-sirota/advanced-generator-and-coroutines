import time
from collections import namedtuple
from datetime import datetime
from queue import Queue
from threading import Thread

import numpy as np

from module4 import coroutine


def run_target(queue, target):
    while True:
        item = queue.get()
        if item is GeneratorExit:
            target.close()
            return
        else:
            try:
                target.send(item)
            except StopIteration as e:
                coprint(f'Dispatcher: Got exception, its value is {e.value}')


@coroutine
def threaded(target):
    messages = Queue()
    Thread(target=run_target, args=(messages, target)).start()
    try:
        while True:
            item = yield
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)


def coprint(msg):
    print(f'{datetime.utcnow()}:{msg}')


@coroutine
def broadcast(targets):
    for target in targets:
        next(target)  # Prime targets
    while True:
        item = yield
        np.random.choice(np.array(targets)).send(item)


def dispatch_work(int_list, targets):
    broadcaster = broadcast(targets)
    array = np.array(int_list)
    subarrays_number = len(array) / 4 + 1
    subarrays = np.array_split(array, subarrays_number)
    coprint(f'Dispatcher: Subarrays to send are {subarrays}')
    for subarray in subarrays:
        coprint(f'Dispatcher: Sending subarray {subarray}')
        broadcaster.send(subarray)
    coprint(f'Dispatcher: Subarrays sent, ending!')
    broadcaster.send(None)


def good_worker(target, worker_id=1):
    coprint(f'Good worker {worker_id}: Time to work!')
    while True:
        subarray = yield
        coprint(f'Good worker {worker_id}: Got: {subarray}')
        try:
            if subarray is None:
                target.send(subarray)
            else:
                target.send(sum(subarray))
        except StopIteration as e:
            raise e


def slow_worker(target, worker_id=1):
    coprint(f'Slow worker {worker_id}: Time to work!')
    while True:
        subarray = yield
        coprint(f'Slow worker {worker_id}: Got: {subarray}')
        time.sleep(5)
        try:
            if subarray is None:
                target.send(subarray)
            else:
                target.send(sum(subarray))
        except StopIteration as e:
            raise e


@coroutine
def accumulator():
    coprint(f'Accumulator : Time to accumulate!')
    result = namedtuple('Sum', ['sum'])
    add = 0
    while True:
        value = yield
        if value is None:
            coprint(f'Accumulator : Got None, reporting!')
            break
        coprint(f'Accumulator : Got {value}!')
        add += value
    coprint(f'Accumulator: Final result was {result(sum=add)}')
    return result(sum=add)


def dispatch_workers(number_of_good=1, number_of_slow=0):
    arraylist = np.random.randint(0, 10, size=20)
    coprint(f'Array: {arraylist} and its sum is {sum(arraylist)}')
    accumulate = accumulator()
    targets = []
    for i in range(number_of_good):
        targets.append(threaded(good_worker(accumulate, worker_id=i)))
    for i in range(number_of_slow):
        targets.append(threaded(slow_worker(accumulate, worker_id=i)))
    dispatch_work(arraylist, targets)


if __name__ == '__main__':
    dispatch_workers(2, 1)
