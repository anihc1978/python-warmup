"""
05_generators.py
IBM Python Warm-up — Generators & Iterators
"""
from __future__ import annotations
from typing import Generator, Iterator
import itertools


def countdown(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1


def fibonacci() -> Generator[int, None, None]:
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def running_average(data: list[float]) -> Generator[float, None, None]:
    total = 0.0
    for i, val in enumerate(data, start=1):
        total += val
        yield total / i


def read_in_chunks(text: str, chunk_size: int = 20) -> Generator[str, None, None]:
    for i in range(0, len(text), chunk_size):
        yield text[i: i + chunk_size]


class RangeIterator:
    """Custom iterator mimicking range()."""

    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    print("Countdown:", list(countdown(5)))

    fib = fibonacci()
    first_10 = [next(fib) for _ in range(10)]
    print("Fibonacci:", first_10)

    prices = [8.5, 9.0, 7.5, 10.0, 8.0]
    print("Running avg:", [round(v, 2) for v in running_average(prices)])

    sample = "Hello from the generator world!"
    print("Chunks:", list(read_in_chunks(sample, 10)))

    r = RangeIterator(0, 10, 2)
    print("Custom range:", list(r))

    chained = list(itertools.islice(itertools.chain(countdown(3), fibonacci()), 8))
    print("Chain + islice:", chained)

    print("Generators demo complete.")
