def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def my_coroutine(a):
    print(f'--> Started with {a}')
    b = yield
    print(f'But continues with {b}')