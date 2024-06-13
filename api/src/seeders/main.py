from .memo import memo_seeder
from .company import company_seeder

def main():
    memo_seeder()
    company_seeder()

if __name__ == "__main__":
    main()