from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.database import engine, create_db_and_tables
from api.endpoints.calc import router as calc_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(calc_router, prefix="/calc")

@app.get("/")
async def root():
    return {"message": "Calculation Service"}
