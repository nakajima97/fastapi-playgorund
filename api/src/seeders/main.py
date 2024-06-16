from .memo import memo_seeder
from .company import company_seeder
from .user import user_seeder


def main():
    company_seeder()
    user_seeder()
    memo_seeder()


if __name__ == "__main__":
    main()
