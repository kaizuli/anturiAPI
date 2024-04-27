from .schemas import SensorDB, TemperatureDB  # , SectionEnums
from sqlmodel import Session, select

def get_sensors(session: Session):
    return session.exec(select(SensorDB)).all()

def get_sensor(session: Session, id: int):
    return session.get(SensorDB, id)

def get_sections_sensors(session: Session, section: str):
    return session.exec(select(SensorDB)
                        .filter_by(section=section)).all()

def get_sensors_by_status(session: Session, status: int):
    return session.exec(select(SensorDB)
                        .filter_by(status=status)).all()

# list sensor updates

