from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.cruds.memo import fetch_memo, count_memos

router = APIRouter()

@router.get("/memo")
async def get_memo(limit: int = 10, offset:int = 0, db: Session = Depends(get_db)):
  data = fetch_memo(db, limit=limit, offset=offset)
  count = count_memos(db)
  return {'data': data, 'count': count}