from fastapi import HTTPException
from .models import SensorDB, SensorCreate #, SectionEnums
from sqlmodel import Session, select

def create_sensor(session: Session, sensor_in: SensorCreate):
    sensordb = SensorDB.model_validate(sensor_in)
    session.add(sensordb)
    session.commit()
    session.refresh(sensordb)
    return sensordb

def get_sensors(session: Session):
    return session.exec(select(SensorDB)).all()

def get_sections_sensors(session: Session, section):
    # logic for filtering sensors by the section
    pass

def get_sensor(session: Session, id: int):
    sensor = session.get(SensorDB, id)
    # default top(10)
    # filter between (time,time)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {id} not found.')
    return sensor # AND temps based on filters

# def update_sensor_status

# list sensor updates

# list statuses
