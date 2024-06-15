from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.cruds.fetch_company_users import fetch_company_users_with_joinedload, fetch_company_users_with_join
from src.db import get_db

router = APIRouter()

company_user_tag = "/company/users"

@router.get("/company/users/joinload", tags=[company_user_tag], description="joinedloadを使って会社のユーザーを取得します。")
async def get_company_users(db: Session = Depends(get_db), company_id: int = 1):
    users = fetch_company_users_with_joinedload(db, company_id)
    return {"data": users}

@router.get('/company/users/join', tags=[company_user_tag], description="joinを使って会社のユーザーを取得します。")
async def get_company_users(db: Session = Depends(get_db), company_id: int = 1):
    users = fetch_company_users_with_selectinload(db, company_id)
    return {"data": users}