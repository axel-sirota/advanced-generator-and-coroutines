from module4 import coroutine


@coroutine
def filter_by_pattern(pattern, target):
    print(f'I am going to filter lines by pattern {pattern}')
    while True:
        line = yield
        if pattern in line:
            target.send(line)


def iterate_file(file, target):
    with open(file) as f:
        for line in f:
            target.send(line)
    print('Im done!')


@coroutine
def coprint():
    while True:
        line = yield
        print(f'-->{line}\n')


