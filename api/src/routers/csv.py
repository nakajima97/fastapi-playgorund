from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/csv")
async def get_csv():
    content = "id,name\n1,John\n2,Doe"
    filename = "sample.csv"

    headers = {
        "Content-Type": "text/csv",
        "Content-Disposition": f"attachment; filename={filename}",
    }

    return Response(content, headers=headers)
