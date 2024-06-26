from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from src.db import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    users = relationship("User", backref="company")
