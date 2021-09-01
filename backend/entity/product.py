from flask import Flask, abort, request
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, PositiveInt, PositiveFloat, validator

class Product(BaseModel):
  sku: PositiveInt
  name: str
  description: Optional[str]
  brand: str
  price: PositiveFloat
  weight: PositiveFloat
  category: str
  stock: PositiveInt
  thumbnail_url: str
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