"""
08_error_handling.py
IBM Python Warm-up — Exceptions, custom errors, context managers
"""
from __future__ import annotations
from typing import Optional
import contextlib
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


# --- Custom exception hierarchy ---

class AppError(Exception):
    """Base application error."""
    def __init__(self, message: str, code: int = 0) -> None:
        super().__init__(message)
        self.code = code


class ValidationError(AppError):
    pass


class NotFoundError(AppError):
    pass


# --- Functions using try/except/else/finally ---

def safe_divide(a: float, b: float) -> Optional[float]:
    try:
        result = a / b
    except ZeroDivisionError:
        logger.warning("Division by zero attempted.")
        return None
    except TypeError as e:
        raise ValidationError(f"Invalid types: {e}", code=400) from e
    else:
        logger.info("Division succeeded: %s", result)
        return result
    finally:
        logger.debug("safe_divide called with a=%s, b=%s", a, b)


def fetch_item(db: dict, key: str) -> str:
    try:
        return db[key]
    except KeyError:
        raise NotFoundError(f"Key '{key}' not found.", code=404)


# --- Context manager using class ---

class Timer:
    import time as _time

    def __enter__(self) -> Timer:
        self.start = self._time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        elapsed = self._time.perf_counter() - self.start
        logger.info("Elapsed: %.4f s", elapsed)
        return False  # do not suppress exceptions


# --- Context manager using contextlib ---

@contextlib.contextmanager
def managed_resource(name: str):
    logger.info("Acquiring: %s", name)
    try:
        yield name.upper()
    except Exception as e:
        logger.error("Error in resource %s: %s", name, e)
        raise
    finally:
        logger.info("Releasing: %s", name)


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    try:
        fetch_item({"a": 1}, "b")
    except NotFoundError as e:
        print(f"Caught: {e} (code={e.code})")

    with Timer():
        _ = sum(range(1_000_000))

    with managed_resource("database_connection") as res:
        print("Using resource:", res)

    print("Error handling demo complete.")
