from fastapi import FastAPI
import uvicorn
import os
from app.api.routers import api_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="HomeFinance",
    debug=False,
)
app.include_router(api_router,prefix="/homefinance")
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=os.getenv("APP_HOST"), port=os.getenv("APP_PORT"), reload=True)