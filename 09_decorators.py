"""
09_decorators.py
IBM Python Warm-up — Decorators (function, class, parameterised, stacking)
"""
from __future__ import annotations
import time
import functools
import logging
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# 1. Simple decorator — timing
def timer(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        logger.info("%s took %.4fs", func.__name__, time.perf_counter() - t0)
        return result
    return wrapper  # type: ignore[return-value]


# 2. Decorator with parameters — retry
def retry(times: int = 3, exceptions: tuple = (Exception,)):
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning("Attempt %d/%d failed: %s", attempt, times, e)
                    if attempt == times:
                        raise
        return wrapper  # type: ignore[return-value]
    return decorator


# 3. Class-based decorator — call counter
class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        logger.info("Call #%d to %s", self.calls, self.func.__name__)
        return self.func(*args, **kwargs)


# 4. Stacking decorators
@timer
@CountCalls
def compute(n: int) -> int:
    """Sum of squares up to n."""
    return sum(i * i for i in range(n))


@retry(times=3, exceptions=(ValueError,))
def flaky_parse(value: str) -> int:
    result = int(value)
    if result < 0:
        raise ValueError("Negative not allowed")
    return result


if __name__ == "__main__":
    print("compute(1000):", compute(1000))
    print("compute(500):", compute(500))
    print("Calls so far:", compute.func.calls)  # type: ignore[attr-defined]

    print("Parse '42':", flaky_parse("42"))
    try:
        flaky_parse("abc")
    except ValueError as e:
        print("Expected error:", e)

    print("Decorators demo complete.")
