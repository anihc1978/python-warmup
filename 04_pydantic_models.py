"""
04_pydantic_models.py
IBM Python Warm-up — Pydantic v2 Models & Validation
"""
from __future__ import annotations
from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
from pydantic import ValidationError
from typing import Optional
from datetime import date
from enum import Enum


class Category(str, Enum):
    FOOD = "food"
    BEVERAGE = "beverage"
    HOUSEHOLD = "household"


class SKU(BaseModel):
    code: str = Field(..., pattern=r"^[A-Z]{2}-\d{4}$", description="Format: XX-0000")
    name: str = Field(..., min_length=2, max_length=80)
    category: Category
    price: float = Field(..., gt=0, description="Price in USD, must be positive")
    stock: int = Field(default=0, ge=0)
    expiry_date: Optional[date] = None

    @field_validator("name")
    @classmethod
    def title_case_name(cls, v: str) -> str:
        return v.title()

    @model_validator(mode="after")
    def expiry_required_for_food(self) -> SKU:
        if self.category == Category.FOOD and self.expiry_date is None:
            raise ValueError("Food items must have an expiry date.")
        return self


class Supplier(BaseModel):
    supplier_id: int
    company_name: str
    contact_email: EmailStr
    skus: list[SKU] = []

    model_config = {"frozen": False, "str_strip_whitespace": True}


if __name__ == "__main__":
    sku = SKU(
        code="AC-1234",
        name="aceite de oliva extra virgen",
        category=Category.FOOD,
        price=12.99,
        stock=50,
        expiry_date=date(2026, 12, 31),
    )
    print(sku.model_dump())
    print("Name (title-cased):", sku.name)

    try:
        bad = SKU(code="bad", name="X", category=Category.FOOD, price=-1)
    except ValidationError as e:
        print("Validation errors:", e.error_count())

    supplier = Supplier(
        supplier_id=1,
        company_name="  Distribuidora Norte  ",
        contact_email="contact@norte.cl",
        skus=[sku],
    )
    print("Supplier:", supplier.company_name, "| SKUs:", len(supplier.skus))
    print("Pydantic models demo complete.")
