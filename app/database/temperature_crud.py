from fastapi import HTTPException
from .models import TemperatureDB, TemperatureCreate
from sqlmodel import Session

def create_temp(session: Session, temp_in: TemperatureCreate):
    temperaturedb = TemperatureDB.model_validate(temp_in)
    session.add(temperaturedb)
    session.commit()
    session.refresh(temperaturedb)
    return temperaturedb

def delete_temp(session: Session, id: int):
    temp = session.get(TemperatureDB, id)
    if not temp:
        raise HTTPException(status_code=404, detail=f'Temperature measurement with id {id} not found.')
    session.delete(temp)
    session.commit()
    return {'message': f'Temperature measurement with id {id} deleted.'}
