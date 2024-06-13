from .memo import memo_seeder
from .company import company_seeder
from .user import user_seeder


def main():
    memo_seeder()
    company_seeder()
    user_seeder()


if __name__ == "__main__":
    main()
