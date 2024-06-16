from sqlalchemy.orm import Session
from faker import Faker
from src.models.user import User
from src.db import db_engine

from .company import company_count

# fakerインスタンスを作成します
fake = Faker("jp-JP")

user_count = 100


def user_seeder():
    # SQLAlchemy sessionを作成します
    with Session(db_engine) as session:
        # 100回ループします
        for _ in range(user_count):
            # ダミーデータを生成します
            fake_user = User(
                name=fake.name(), company_id=fake.random_int(min=1, max=company_count)
            )

            # データをテーブルに挿入します
            session.add(fake_user)

        # 変更をコミットします
        session.commit()
