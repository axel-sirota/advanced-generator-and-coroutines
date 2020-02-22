#  Example from Dave Beazley
from module4.coroutine_decorator import coroutine


@coroutine
def pattern(language):
    print(f'I only react to {language} messages')
    while True:
        line = yield
        try:
            if language in line:
                print(line)
        except TypeError:
            print('Please send me a string message')
