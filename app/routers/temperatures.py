from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database import temperature_crud
from ..database.database import get_session
from ..database.schemas import TemperatureDB, TemperatureCreate

router = APIRouter(prefix='/temperatures')

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_temp(*, session: Session = Depends(get_session), temp_in: TemperatureCreate):
    return temperature_crud.create_temp(session, temp_in)

@router.delete('/{id}')
def delete_temp(*, session: Session = Depends(get_session), id: int):
    return temperature_crud.delete_temp(session, id)
