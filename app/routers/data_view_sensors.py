from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from ..database import data_view_crud
from ..database.database import get_session
from ..database.schemas import SensorDB, TemperatureDB
from ..database.models import SensorWithTemperatures, SectionsSensors

router = APIRouter(prefix='/sensors')

@router.get('/', response_model=list[SensorDB])
def list_sensors(*, session: Session = Depends(get_session)):
    return data_view_crud.get_sensors(session)

@router.get('/{id}/temperatures', response_model=SensorWithTemperatures)
def get_sensor_with_temps(*, session: Session = Depends(get_session), sensor_id: int, size: int = 10, start_time: datetime = None, end_time: datetime = None):
    sensor = data_view_crud.get_sensor(session, sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {sensor_id} not found.')
    # base query
    query = session.query(TemperatureDB).filter_by(sensorid=sensor_id).order_by(TemperatureDB.timestamp)

    # filter between (time,time)
    if start_time and end_time:
        query = query.filter(start_time <= TemperatureDB.timestamp <= end_time)

    elif start_time:
        query = query.filter(start_time <= TemperatureDB.timestamp)

    elif end_time:
        query = query.filter(TemperatureDB.timestamp <= end_time)

    # add size limit to values
    temperatures = query.limit(size).all()

    # make the temperature pairs
    temperature_pairs = [(temp.temp, temp.timestamp) for temp in temperatures]

    # insert values to model
    sensor_with_temps = SensorWithTemperatures(
        id=sensor.id,
        section=sensor.section,
        status=sensor.status,
        temp_timestamp_pairs=temperature_pairs
    )
    return sensor_with_temps

@router.get('/status/{status}', response_model=list[SensorDB])
def list_sensors_by_status(*, session: Session = Depends(get_session), status: int):
    return data_view_crud.get_sensors_by_status(session, status)

@router.get('/section/{section}', response_model=list[SectionsSensors])
def list_sensors_by_section(*, session: Session = Depends(get_session), section: str):
    sensors = data_view_crud.get_sections_sensors(session, section)
    if not sensors:
        raise HTTPException(status_code=404, detail=f'Section called {section} not found.')
    sensors_with_temperatures = []
    for sensor in sensors:
        temperature = session.exec(select(TemperatureDB)
                                   .filter_by(sensorid=sensor.id)
                                   .order_by(TemperatureDB.timestamp)
                                   .limit(1)
                                   ).first()
        if temperature:
            sensor_with_temperature = SectionsSensors(
                id=sensor.id,
                status=sensor.status,
                temperature=temperature.temp,
                timestamp=temperature.timestamp
            )
            sensors_with_temperatures.append(sensor_with_temperature)
    return sensors_with_temperatures
