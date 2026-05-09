"""
07_classes_and_protocols.py
IBM Python Warm-up — OOP, ABCs, Protocols, and dunder methods
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Serializable(Protocol):
    def to_dict(self) -> dict: ...


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(area={self.area():.2f})"


class Circle(Shape):
    PI = 3.141592653589793

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return self.PI * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * self.PI * self.radius

    def to_dict(self) -> dict:
        return {"type": "circle", "radius": self.radius}


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def to_dict(self) -> dict:
        return {"type": "rectangle", "width": self.width, "height": self.height}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __hash__(self) -> int:
        return hash((self.width, self.height))


if __name__ == "__main__":
    shapes: list[Shape] = [Circle(5), Rectangle(4, 6), Circle(3)]
    for s in shapes:
        print(s, "| perimeter:", round(s.perimeter(), 2))

    c = Circle(5)
    print("Is Serializable:", isinstance(c, Serializable))
    print("Dict:", c.to_dict())

    r1, r2 = Rectangle(4, 6), Rectangle(4, 6)
    print("Equal:", r1 == r2)
    print("Classes and Protocols demo complete.")
