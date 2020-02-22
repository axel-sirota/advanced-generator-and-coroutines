class GenkidamaException(BaseException):
    pass


def caller():
    mygen = delegating_gen()
    print(f'-->{next(mygen)}')
    print(f'-->{next(mygen)}')
    try:
        print(f'--> Take my ValueError subgen!')
        mygen.throw(ValueError)
    except GenkidamaException:
        print(f'-->I got your genkidama! \n Now I will close you')
        mygen.close()


def delegating_gen():
    print(f'**> I am the delegating gen, I dont do much here!')
    try:
        yield from subgen()
    except ValueError:
        print('** I got a Value Error')


def subgen():
    try:
        print(f'I am a subgenerator and I am yielding!')
        print(f'I will yield 1')
        yield 1
        print(f'I will yield 2')
        yield 2
        print(f'I will yield 3')
        yield 3
        print(f'I am done!')
    except ValueError:
        print('HA! I got you! Get my Genkidama caller!')
        raise GenkidamaException('Take that!')
