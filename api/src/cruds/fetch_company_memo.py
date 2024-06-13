from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

from src.models.company import Company as company_model
from src.models.user import User as user_model
from src.models.memo import Memo as memo_model

def fetch_company_memos(db: Session, company_id: int):
    query = db.execute(
        select(company_model).options(
            joinedload(company_model.users)
            .joinedload(user_model.memos)
        ).where(company_model.id == company_id)
    )
    result = query.unique().all()

    return result