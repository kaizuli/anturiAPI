from decimal import Decimal
from datetime import datetime
from sqlmodel import SQLModel
from typing import List
from .schemas import SensorDB, TemperatureDB

class SensorWithTemperatures(SQLModel):
    id: int
    section: str
    status: int
    temperatures: List[Decimal]
    timestamps: List[datetime]
