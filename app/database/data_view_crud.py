from .schemas import SensorDB, TemperatureDB  # , SectionEnums
from sqlmodel import Session, select

def get_sensors(session: Session):
    return session.exec(select(SensorDB)).all()

def get_sections_sensors(session: Session, section):
    # logic for filtering sensors by the section
    pass


