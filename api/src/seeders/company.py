from sqlalchemy.orm import Session
from faker import Faker
from src.models.company import Company
from src.db import db_engine

# fakerインスタンスを作成します
faker = Faker("jp-JP")

company_count = 10

def company_seeder():
    # SQLAlchemy sessionを作成します
    with Session(db_engine) as session:
        # 100回ループします
        for _ in range(company_count):
            # ダミーデータを生成します
            fake_company = Company(
                name=faker.company() # ダミーテキストを生成します
            )

            # データをテーブルに挿入します
            session.add(fake_company)

        # 変更をコミットします
        session.commit()
