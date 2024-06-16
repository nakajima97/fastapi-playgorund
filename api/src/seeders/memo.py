from sqlalchemy.orm import Session
from faker import Faker
from src.models.memo import Memo
from src.db import db_engine

from .user import user_count

# fakerインスタンスを作成します
fake = Faker("jp-JP")


def memo_seeder():
    # SQLAlchemy sessionを作成します
    with Session(db_engine) as session:
        # 100回ループします
        for _ in range(200):
            # ダミーデータを生成します
            fake_memo = Memo(
                content=fake.text(),
                user_id=fake.random_int(1, user_count),
                created_at=fake.date_between(start_date="-1y", end_date="today"),
            )

            # データをテーブルに挿入します
            session.add(fake_memo)

        # 変更をコミットします
        session.commit()
