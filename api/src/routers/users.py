from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.cruds.fetch_company_users import (
    fetch_company_users_with_joinedload,
    fetch_company_users_with_join,
)
from src.db import get_db

router = APIRouter()

company_user_tag = "/company/users"


@router.get(
    "/company/users/joinedload",
    tags=[company_user_tag],
    name="joinedloadを使って会社のユーザーを取得する",
)
async def get_company_users_joinedload(
    db: Session = Depends(get_db), company_id: int = 1
):
    users = fetch_company_users_with_joinedload(db, company_id)
    return {"data": users}


@router.get(
    "/company/users/join",
    tags=[company_user_tag],
    name="joinを使って会社のユーザーを取得する",
    description="joinを使ってjoinendloadで結合した場合と同じように値を取得する",
)
async def get_company_users_join(db: Session = Depends(get_db), company_id: int = 1):
    company = fetch_company_users_with_join(db, company_id)

    # companyはCompanyクラスのインスタンスなので、dictに変換してusersを追加する
    company_dict = company.__dict__
    company_dict["users"] = company.users

    # joinedloadで一発で取得した際はリストで返ってくるので、同じになるようリストに変換して返す
    return {"data": [company]}
