def mybomb(count):
    print(f'Activating the bomb and it will explode in {count} seconds')
    while count > 0:
        yield count
        count -= 1
    print('BAM!!')