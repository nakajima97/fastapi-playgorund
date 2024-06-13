from sqlalchemy import Column, Integer, Text

from src.db import Base


class Memo(Base):
    __tablename__ = "memos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
