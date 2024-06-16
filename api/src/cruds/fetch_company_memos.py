from sqlalchemy.orm import Session, joinedload, contains_eager
from datetime import datetime

from src.models.company import Company as company_model
from src.models.user import User as user_model
from src.models.memo import Memo as memo_model


def fetch_company_memos_with_joinedload(db: Session, company_id: int):
    """joinedloadを使ってメモの一覧を取得する関数

    """
    query = db.query(company_model).options(
        joinedload(company_model.users)
        .joinedload(user_model.memos)
    ).filter(company_model.id == company_id)

    result = query.all()

    return result

def fetch_company_memos_with_join(db: Session, company_id: int):
    """joinを使ってメモの一覧を取得する関数
    """

    query = db.query(company_model).join(company_model.users).join(user_model.memos).filter(company_model.id == company_id)

    company = query.all()

    return company

def fetch_company_memos_with_join_filter(db: Session, company_id: int, start_date: datetime = None, end_date: datetime = None):
    """joinを使ってメモの一覧を取得する関数
    """

    query = db.query(company_model).join(company_model.users).join(user_model.memos)\
        .options(contains_eager(company_model.users).contains_eager(user_model.memos))\
        .filter(company_model.id == company_id)

    if start_date:
        query = query.filter(memo_model.created_at >= start_date)

    if end_date:
        query = query.filter(memo_model.created_at <= end_date)

    company = query.all()

    return company