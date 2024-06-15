from sqlalchemy.orm import Session, joinedload
from src.models.company import Company

def fetch_company_users_with_joinedload(db: Session, company_id: int):
    return db.query(Company).options(joinedload(Company.users)).filter(Company.id == company_id).all()