from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.cruds.memo import fetch_memo

router = APIRouter()

@router.get("/memo")
async def get_memo(db: Session = Depends(get_db)):
  return fetch_memo(db)