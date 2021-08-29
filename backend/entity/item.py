from flask import Flask, abort, request
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, PositiveInt, PositiveFloat, validator
from enum import Enum

class FulfilmentState(int, Enum):
    IN_INVENTORY="IN_INVENTORY"
    EXPIRED="EXPIRED"
    SHIPPED="SHIPPED"

class Item(BaseModel):
        id: int
        sku_id: int
        reception_date: str
        removal_date: Optional[str]  # should be optional
        state: FulfilmentState