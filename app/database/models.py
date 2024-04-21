from datetime import datetime
from decimal import Decimal
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional

# class SectionEnums(Enum):
#     A13_13: 1
#     B1_2: 2
#     A14_0: 3
#
# class StatusEnums(Enum):
#     OK: 1
#     ERROR: 0

class SensorBase(SQLModel):
    section: Optional[str]
    status: int

class SensorDB(SensorBase, table=True):
    id: int = Field(default=None, primary_key=True)
    status: int = Field(default=1)

class SensorCreate(SensorBase):
    pass

class TemperatureBase(SQLModel):
    sensorid: int
    temp: Decimal

class TemperatureDB(TemperatureBase, table=True):
    id: int = Field(default=None, primary_key=True)
    sensorid: int = Field(default=None, foreign_key='sensordb.id')
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    temp: Decimal = Field(default=None, decimal_places=1)
    error: str | None = Field(default=None)

class TemperatureCreate(TemperatureBase):
    pass
