"""
03_dataclasses.py
IBM Python Warm-up — dataclasses (PEP 557)
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar


@dataclass
class Point:
    x: float
    y: float

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


@dataclass(order=True)
class Product:
    sort_index: float = field(init=False, repr=False)
    name: str
    price: float
    stock: int = 0
    tags: list[str] = field(default_factory=list)
    TAX_RATE: ClassVar[float] = 0.19

    def __post_init__(self) -> None:
        self.sort_index = self.price

    @property
    def price_with_tax(self) -> float:
        return round(self.price * (1 + self.TAX_RATE), 2)


@dataclass(frozen=True)
class ImmutableVector:
    x: float
    y: float
    z: float = 0.0

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


if __name__ == "__main__":
    p = Point(3.0, 4.0)
    print(f"Point: {p}, distance: {p.distance_to_origin()}")

    prod = Product("Aceite de oliva", 8.50, stock=120, tags=["grocery", "oil"])
    print(f"Product: {prod}")
    print(f"Price with tax: {prod.price_with_tax}")
    print(f"As dict: {asdict(prod)}")

    products = [
        Product("Vinagre", 2.30),
        Product("Sal", 0.90),
        Product("Azucar", 1.20),
    ]
    products.sort()
    print("Sorted:", [p.name for p in products])

    v = ImmutableVector(1.0, 2.0, 2.0)
    print(f"Vector magnitude: {v.magnitude()}")
    print("Dataclasses demo complete.")
