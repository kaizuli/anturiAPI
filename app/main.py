from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import sensors, temperatures
from .database.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting')
    create_db()
    yield
    print('Ending session')

app = FastAPI(lifespan=lifespan)

app.include_router(sensors.router)
app.include_router(temperatures.router)

