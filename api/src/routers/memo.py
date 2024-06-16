from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from src.db import get_db
from src.cruds.memo import fetch_memo, count_memos
from src.cruds.fetch_company_memos import fetch_company_memos_with_joinedload, fetch_company_memos_with_join, fetch_company_memos_with_join_filter

router = APIRouter()


company_memo_tag = "/company/memo"

@router.get("/memo")
async def get_memo(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    data = fetch_memo(db, limit=limit, offset=offset)
    count = count_memos(db)
    return {"data": data, "count": count}


@router.get(
    "/company/{company_id}/memo/joinedload",
    tags=[company_memo_tag],
    name="joinedloadを使ってmemoを取得"
)
async def get_company_memo_with_joinedload(company_id: int = 1, db: Session = Depends(get_db)):
    data = fetch_company_memos_with_joinedload(db, company_id)

    return {"data": data}

@router.get(
    "/company/{company_id}/memo/join",
    tags=[company_memo_tag],
    name="joinを使ってmemoを取得"
)
async def get_company_memo_with_joinedload(company_id: int = 1, db: Session = Depends(get_db)):
    company = fetch_company_memos_with_join(db, company_id)

    users = company[0].users
    company_dict = company[0].__dict__
    company_dict["users"] = []

    for user in users:
        user_dict = user.__dict__
        user_dict["memos"] = user.memos
        company_dict["users"].append(user_dict)

    return {"data": [company_dict]}

@router.get(
    "/company/{company_id}/memo/join/filter",
    tags=[company_memo_tag],
    name="joinを使ってmemoを取得。日付で絞り込みが可能。"
)
async def get_company_memo_with_joinedload(start_date: datetime = None, end_date: datetime = None, company_id: int = 1, db: Session = Depends(get_db)):
    company = fetch_company_memos_with_join_filter(db, company_id, start_date, end_date)

    users = company[0].users
    company_dict = company[0].__dict__
    company_dict["users"] = []

    for user in users:
        user_dict = user.__dict__
        user_dict["memos"] = user.memos
        company_dict["users"].append(user_dict)

    return {"data": [company_dict]}