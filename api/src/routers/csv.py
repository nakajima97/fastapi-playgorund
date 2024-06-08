from fastapi import APIRouter

router = APIRouter()

@router.get("/csv")
async def get_csv():
    return {"message": "Hello World"}