from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.cruds.memo import fetch_memo, count_memos
from src.cruds.fetch_company_memos import fetch_company_memos_with_joinedload

router = APIRouter()


company_memo_tag = "/company/memo"

@router.get("/memo")
async def get_memo(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    data = fetch_memo(db, limit=limit, offset=offset)
    count = count_memos(db)
    return {"data": data, "count": count}


@router.get(
    "/company/{company_id}/memo",
    tags=[company_memo_tag],
    name="joinedloadを使ってmemoを取得"
)
async def get_company_memo(company_id: int = 1, db: Session = Depends(get_db)):
    data = fetch_company_memos_with_joinedload(db, company_id)

    return {"data": data}
