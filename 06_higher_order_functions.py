"""
06_higher_order_functions.py
IBM Python Warm-up — Higher-Order Functions, map/filter/reduce, functools
"""
from __future__ import annotations
from typing import Callable, TypeVar
from functools import reduce, partial, lru_cache
import operator

T = TypeVar("T")
U = TypeVar("U")


def compose(*funcs: Callable) -> Callable:
    """Right-to-left function composition."""
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed


def pipe(*funcs: Callable) -> Callable:
    """Left-to-right function piping."""
    def piped(x):
        for f in funcs:
            x = f(x)
        return x
    return piped


def memoize(func: Callable) -> Callable:
    """Simple memoization decorator."""
    cache: dict = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def apply_twice(func: Callable[[T], T], value: T) -> T:
    return func(func(value))


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # map / filter / reduce
    doubled = list(map(lambda x: x * 2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    total = reduce(operator.add, nums)
    print("Doubled:", doubled)
    print("Evens:", evens)
    print("Sum:", total)

    # partial
    add5 = partial(operator.add, 5)
    print("Add 5:", list(map(add5, [1, 2, 3])))

    # compose & pipe
    normalize = compose(str.strip, str.lower, str.title)
    print("Composed:", normalize("  ACEITE DE OLIVA  "))

    pipeline = pipe(lambda x: x + 1, lambda x: x * 2, str)
    print("Piped:", pipeline(4))

    # apply_twice
    print("Apply twice (x*2):", apply_twice(lambda x: x * 2, 3))

    # lru_cache factorial
    print("10!:", factorial(10))

    print("Higher-order functions demo complete.")
