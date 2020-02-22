from module4.coroutine_decorator import coroutine


@coroutine
def coroutine_yield(a):
    print(f'--> Started with {a}')
    b = yield a
    print(f'However I got sent a {b} and yielded back {a}')
    c = a + b
    yield c
    print(f'I yielded back a {c} and exited')

