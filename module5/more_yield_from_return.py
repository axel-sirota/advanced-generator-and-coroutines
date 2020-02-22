def caller():
    mygen = delegating_gen()
    while True:
        try:
            print(f'Next value: {next(mygen)}')
        except StopIteration as e:
            print(f'Caller print: {e.value}')
            break


def delegating_gen():
    try:
        magic_value = yield from subgen()
    except StopIteration as e:
        print(f'Delegating generator print: {e.value}')
    else:
        print(f'Delegating generator final print:{magic_value}')
        return 'Goodbye'


def subgen():
    yield 1
    yield 2
    return 'Hello'
