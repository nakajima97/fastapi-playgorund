from fastapi import FastAPI
from src.routers import hello, csv, memo, users, ws

app = FastAPI()

app.include_router(hello.router)
app.include_router(csv.router)
app.include_router(memo.router)
app.include_router(users.router)
app.include_router(ws.router)