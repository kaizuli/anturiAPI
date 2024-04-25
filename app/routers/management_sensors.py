from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session
from ..database import sensor_management_crud
from ..database.database import get_session
from ..database.schemas import SensorCreate

router = APIRouter(prefix='/sensors')

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_sensor(*, session: Session = Depends(get_session), sensor_in: SensorCreate):
    sensor = sensor_management_crud.create_sensor(session, sensor_in)
    return {'message': f'Sensor with id {sensor.id} created'}

@router.patch('/{id}/status', status_code=status.HTTP_200_OK)
def update_sensor_status(*, session: Session = Depends(get_session), sensor_id: int, status: int = 1):
    sensor = sensor_management_crud.update_sensor_status(session, sensor_id, status)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {sensor_id} not found.')
    return {'message': f'Sensor with id {sensor_id} status updated to {status}'}

@router.patch('/{id}/section', status_code=status.HTTP_200_OK)
def update_sensor_section(*, session: Session = Depends(get_session), sensor_id: int, section: str):
    sensor = sensor_management_crud.update_sensor_section(session, sensor_id, section)
    if not sensor:
        raise HTTPException(status_code=404, detail=f'Sensor with id {sensor_id} not found.')
    return {'message': f'Sensor with id {sensor_id} section updated to {section}'}
