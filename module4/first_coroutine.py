def my_coroutine(a):
    print(f'--> Started with {a}')
    b = yield
    print(f'But continues with {b}')
