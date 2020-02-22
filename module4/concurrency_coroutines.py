from threading import Thread
from time import sleep

from module4.coroutine_decorator import coroutine


@coroutine
def my_slow_coroutine():
    print(f'I am so slow')
    yield
    sleep(10)
    print(f'But I am done!')


def run_coroutine(coro):
    try:
        coro.send(None)
    except StopIteration:
        print('Coroutine Done!')


mycoro = my_slow_coroutine()
thread = Thread(target=run_coroutine, args=(mycoro, ))
thread.start()
mycoro.close()
thread.join()
print('Thread done!')

