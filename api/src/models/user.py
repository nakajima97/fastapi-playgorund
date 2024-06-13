from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  company_id = Column(Integer, ForeignKey("companies.id"))
  name = Column(String(255))

  # SQLAlchemyのORMレベルでのリレーションを定義する
  company = relationship("Company", back_populates="users")