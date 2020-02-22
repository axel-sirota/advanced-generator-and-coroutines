import timeit
import numpy as np


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_optimized(n):
    a = 1
    b = 2
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


class FibonacciIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'FibonacciIterable({self.start, self.end})'

    def __iter__(self):
        return FibonacciIterator(self.start, self.end)


class FibonacciIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __next__(self):
        if self.start + self.increment > self.end:
            raise StopIteration()
        fibonacci_number = fibonacci(self.start + self.increment)
        self.increment += 1
        return fibonacci_number

    def __iter__(self):
        return self


class FibonacciGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'FibonacciGenerator({self.start, self.end})'

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield fibonacci(i)


class FibonacciGeneratorOptimized:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'FibonacciGeneratorOptimized({self.start, self.end})'

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield fibonacci_optimized(i)


class FibonacciGeneratorLazyOptimized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.fibonacci_dict = {i: fibonacci_optimized(i) for i in range(self.start, self.end + 1)}
        self.increment = 0

    def __repr__(self):
        return f'FibonacciGeneratorLazyOptimized({self.start, self.end})'

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield self.fibonacci_dict[i]


class FibonacciIterableLazyOptimized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __repr__(self):
        return f'FibonacciIterableLazyOptimized({self.start, self.end})'

    def __iter__(self):
        return FibonacciIteratorLazyOptimized(self.start, self.end)


class FibonacciIteratorLazyOptimized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0
        self.fibonacci_dict = {i: fibonacci_optimized(i) for i in range(self.start, self.end + 1)}

    def __next__(self):
        if self.start + self.increment > self.end:
            raise StopIteration()
        fibonacci_number = self.fibonacci_dict[self.start + self.increment]
        self.increment += 1
        return fibonacci_number

    def __iter__(self):
        return self


class Call:
    def __init__(self, it, start, end):
        self.it = it
        self.start = start
        self.end = end

    def __call__(self, *args, **kwargs):
        for _ in self.it(start=self.start, end=self.end):
            pass


if __name__ == '__main__':
    start_fib = 2
    end_fib = 20
    fibonacci_iterable = FibonacciIterable
    fibonacci_generator = FibonacciGenerator
    fibonacci_generator_lazy = FibonacciGeneratorOptimized
    fibonacci_generator_lazy_fast = FibonacciGeneratorLazyOptimized
    fibonacci_iterable_lazy_fast = FibonacciIterableLazyOptimized
    for iterable in [fibonacci_iterable, fibonacci_generator, fibonacci_generator_lazy, fibonacci_generator_lazy_fast,
                     fibonacci_iterable_lazy_fast]:
        print(f'For the iterable {iterable} we got \n')
        print(f'{np.mean(timeit.repeat(Call(iterable, start_fib, end_fib), number=5, repeat=5))}\n')
