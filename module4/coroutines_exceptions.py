from module4.coroutine_decorator import coroutine


@coroutine
def coroutine_exception(number):
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except ValueError:
            print('*** ValueError handled. Continuing...')
        except GeneratorExit:
            print('This is executed if I get closed, so I need to cleanup here and die gracefully')
            raise
        else:
            print('-> coroutine received: {!r}'.format(x))
            number + x


@coroutine
def coroutine_wihtout_reraise():
    while True:
        try:
            x = yield
        except GeneratorExit:
            print('I do nothing')
        else:
            print(f'Got value {x}')
