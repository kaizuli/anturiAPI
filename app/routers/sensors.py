from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session, select
from ..database import sensor_crud
from ..database.database import get_session
from ..database.schemas import SensorBase, SensorDB, SensorCreate, TemperatureDB
from ..database.models import SensorWithTemperatures

router = APIRouter(prefix='/sensors')

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_sensor(*, session: Session = Depends(get_session), sensor_in: SensorCreate):
    sensor = sensor_crud.create_sensor(session, sensor_in)
    return {'message': f'Sensor with id {sensor.id} created'}

@router.get('/', response_model=list[SensorDB])
def get_sensors(*, session: Session = Depends(get_session)):
    return sensor_crud.get_sensors(session)

@router.get('/{id}', response_model=SensorDB)
def get_sensor(*, session: Session = Depends(get_session), id: int):
    return sensor_crud.get_sensor(session, id)

@router.get('/{id}/temperatures', response_model=SensorWithTemperatures)
def get_sensor_with_temps(*, session: Session = Depends(get_session), sensor_id: int, size: int = 10):
    sensor = sensor_crud.get_sensor(session, sensor_id)
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

@router.patch('/{id}/status', response_model=None)
def update_sensor_status(*, session: Session = Depends(get_session), sensor_id: int, status: int = 1):
    sensor = sensor_crud.update_sensor_status(session, sensor_id, status)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {sensor_id} not found.')
    return {'message': f'Sensor with id {sensor_id} status updated to {status}'}

