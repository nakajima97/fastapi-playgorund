from sqlalchemy.orm import Session
from faker import Faker
from src.models.memo import Memo
from src.db import db_engine

# fakerインスタンスを作成します
fake = Faker("jp-JP")


def memo_seeder():
    # SQLAlchemy sessionを作成します
    with Session(db_engine) as session:
        # 100回ループします
        for _ in range(100):
            # ダミーデータを生成します
            fake_memo = Memo(
                content=fake.text()  # ダミーテキストを生成します
            )

            # データをテーブルに挿入します
            session.add(fake_memo)

        # 変更をコミットします
        session.commit()
