from sqlmodel import Session
from .schemas import SensorDB, SensorCreate  # , SectionEnums

def create_sensor(session: Session, sensor_in: SensorCreate):
    sensordb = SensorDB.model_validate(sensor_in)
    session.add(sensordb)
    session.commit()
    session.refresh(sensordb)
    return sensordb

def update_sensor_status(session: Session, id: int, status: int):
    sensor = session.get(SensorDB, id)
    sensor.status = status
    session.commit()
    return sensor

def update_sensor_section(session: Session, id: int, section: str):
    sensor = session.get(SensorDB, id)
    sensor.section = section
    session.commit()
    return sensor


