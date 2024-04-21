from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database import sensor_crud
from ..database.database import get_session
from ..database.models import SensorBase, SensorDB, SensorCreate

router = APIRouter(prefix='/sensors')

@router.get('/', response_model=list[SensorDB])
def get_sensors(*, session: Session = Depends(get_session)):
    return sensor_crud.get_sensors(session)

@router.get('/{id}', response_model=SensorDB)
def get_sensor(*, session: Session = Depends(get_session), id: int):
    return sensor_crud.get_sensor(session, id)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_sensor(*, session: Session = Depends(get_session), sensor_in: SensorCreate):
    return sensor_crud.create_sensor(session, sensor_in)

