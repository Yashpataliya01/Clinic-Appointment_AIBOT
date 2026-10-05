from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.services.clinic_agent import Database_query


router = APIRouter(prefix="/ai")


class AIQueryRequest(BaseModel):
    question: str


@router.post("/query")
async def query_database(request: AIQueryRequest):

    print("this is the question:", request.question)

    try:

        result = await Database_query(request.question)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        print("AI query error:", e)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to query database"
        )