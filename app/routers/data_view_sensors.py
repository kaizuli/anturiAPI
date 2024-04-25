from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session, select
from ..database import data_view_crud
from ..database.database import get_session
from ..database.schemas import SensorDB, TemperatureDB
from ..database.models import SensorWithTemperatures

router = APIRouter(prefix='/sensors')

@router.get('/', response_model=list[SensorDB])
def list_sensors(*, session: Session = Depends(get_session)):
    return data_view_crud.get_sensors(session)

@router.get('/{id}/temperatures', response_model=SensorWithTemperatures)
def get_sensor_with_temps(*, session: Session = Depends(get_session), sensor_id: int, size: int = 10):
    sensor = data_view_crud.get_sensor(session, sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {sensor_id} not found.')
        # filter between (time,time)
    temperatures = session.exec(select(TemperatureDB)
                                .filter_by(sensorid=sensor_id)
                                .order_by(TemperatureDB.timestamp)
                                .limit(size)
                                ).all()
    temperature_values = [temp.temp for temp in temperatures]
    timestamps = [temp.timestamp for temp in temperatures]

    sensor_with_temps = SensorWithTemperatures(
        id=sensor.id,
        section=sensor.section,
        status=sensor.status,
        temperatures=temperature_values,
        timestamps=timestamps
    )
    return sensor_with_temps

@router.get('/{status}', response_model=list[SensorDB])
def list_sensors_by_status(*, session: Session = Depends(get_session), status: int):
    return data_view_crud.get_sensors_by_status(session, status)
