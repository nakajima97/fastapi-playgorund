from fastapi import APIRouter


router = APIRouter()

@router.get("/company/users")
async def get_company_users():
    return {"message": "Get company users"}