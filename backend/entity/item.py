from flask import Flask, abort, request
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, PositiveInt, PositiveFloat, validator
from uuid import UUID
from enum import Enum

class FulfilmentState(str, Enum):
    IN_INVENTORY="IN_INVENTORY"
    EXPIRED="EXPIRED"
    SHIPPED="SHIPPED"

class Item(BaseModel):
    id: UUID
    sku_id: PositiveInt
    reception_date: str
    removal_date: Optional[str]  # should be optional
    state: FulfilmentState

    @staticmethod
    def from_db(row):
        print(row)
        return Item(
            id=row["id"],
            sku_id=row["sku_id"],
            reception_date=row["reception_date"],
            removal_date=row["removal_date"],
            state=row["state"]
        )