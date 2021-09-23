from typing import Optional
from uuid import UUID
from pydantic import BaseModel, PositiveInt, PositiveFloat


class Product(BaseModel):
    sku: UUID
    name: str
    description: Optional[str]
    brand: str
    price: PositiveFloat
    weight: PositiveFloat
    category: str
    stock: PositiveInt
    thumbnail_url: Optional[str]
    shelf_life: PositiveInt
    active: bool

    @staticmethod
    def from_db(row):
        return Product(
            sku=row["sku"],
            name=row["name"],
            description=row["description"],
            brand=row["brand"],
            price=row["price"],
            weight=row["weight"],
            category=row["category"],
            stock=row["stock"],
            thumbnail_url=row["thumbnail_url"],
            shelf_life=row["shelf_life"],
            active=row["active"]
        )
