from sqlalchemy import create_engine

from src.models.memo import Base

DB_URL = "mysql+pymysql://root@mysql:3306/mydb?charset=utf8"

# echo=True：SQLをログに書く
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    reset_database()