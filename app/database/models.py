from decimal import Decimal
from datetime import datetime
from sqlmodel import SQLModel
from typing import List, Tuple
from .schemas import SensorDB, TemperatureDB

class SensorWithTemperatures(SQLModel):
    id: int
    section: str
    status: int
    temp_timestamp_pairs: List[Tuple[Decimal, datetime]]

class SectionsSensors(SQLModel):
    id: int
    status: int
    temperature: Decimal
    timestamp: datetime

