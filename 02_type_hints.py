"""
02_type_hints.py
IBM Python Warm-up — Type Hints & Annotations (PEP 484 / 526 / 604)
"""
from __future__ import annotations
from typing import Optional, Union, Tuple, Callable, TypeVar, Generic

T = TypeVar("T")


# --- Basic annotations ---

def add(x: int, y: int) -> int:
    return x + y


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def parse_int(value: str) -> Optional[int]:
    """Return int or None if parsing fails."""
    try:
        return int(value)
    except ValueError:
        return None


# --- Union types (Python 3.10+ syntax: X | Y) ---

def stringify(value: int | float | None) -> str:
    if value is None:
        return "N/A"
    return str(value)


# --- Tuple annotations ---

def minmax(data: list[float]) -> Tuple[float, float]:
    return min(data), max(data)


# --- Callable annotations ---

def apply(func: Callable[[int], int], values: list[int]) -> list[int]:
    return [func(v) for v in values]


# --- Generic class ---

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print(add(3, 4))
    print(greet("Eduardo"))
    print(parse_int("42"), parse_int("abc"))
    print(stringify(None), stringify(3.14))
    print(minmax([5, 1, 8, 3]))
    print(apply(lambda x: x * 2, [1, 2, 3, 4]))
    s: Stack[str] = Stack()
    s.push("a"); s.push("b")
    print(s.pop(), len(s))
    print("Type hints demo complete.")
