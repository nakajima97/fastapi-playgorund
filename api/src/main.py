from fastapi import FastAPI
from src.routers import hello, csv

app = FastAPI()

app.include_router(hello.router)
app.include_router(csv.router)
