from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

from src.models.memo import Memo as memo_model


def fetch_memo(db: Session, limit: int = 10, offset: int = 0):
    result: Result = db.execute(
        select(memo_model.id, memo_model.content).limit(limit).offset(offset)
    )
    rows = result.all()
    return [{"id": row[0], "content": row[1]} for row in rows]


def count_memos(db: Session):
    result: Result = db.execute(select(func.count(memo_model.id)))
    count = result.scalar()
    return count
