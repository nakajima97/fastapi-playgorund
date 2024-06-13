from sqlalchemy import Column, Integer, Text

from src.db import Base

class memo(Base):
    __tablename__ = "memo"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)