from sqlalchemy import create_engine

from src.models.memo import Base as MemoBase
from src.models.user import Base as UserBase
from src.models.company import Base as CompanyBase

DB_URL = "mysql+pymysql://root@mysql:3306/mydb?charset=utf8"

# echo=True：SQLをログに書く
engine = create_engine(DB_URL, echo=True)


def reset_database():
    MemoBase.metadata.drop_all(engine)
    UserBase.metadata.drop_all(engine)
    CompanyBase.metadata.drop_all(engine)
    MemoBase.metadata.create_all(engine)
    UserBase.metadata.create_all(engine)
    CompanyBase.metadata.create_all(engine)


if __name__ == "__main__":
    reset_database()
