from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/healthcheck')
async def healthcheck():
    """
        API for server health check up
    """
        
    return JSONResponse(
    status_code=status.HTTP_200_OK,
    content={
        "ok": True,
        "detail": "healthy",
    },
    )