from flask import Flask, abort, request
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, PositiveInt, PositiveFloat, validator

class Product(BaseModel):
        sku: PositiveInt
        description: str
        brand: str
        price: PositiveFloat
        weight: PositiveFloat
        category: str
        stock: PositiveInt
        thumbnail_url: str
        shelf_life: PositiveInt
        active: bool