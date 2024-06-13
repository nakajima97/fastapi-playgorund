from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

from src.models.memo import memo as memo_model

def fetch_memo(db: Session):
    result: Result = db.execute(select(memo_model.id, memo_model.content))
    rows = result.all()
    return [{"id": row[0], "content": row[1]} for row in rows]