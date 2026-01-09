from fastapi import FastAPI
import os

from contextlib import asynccontextmanager
from api.db import init_db
from api.chat import routing as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router.router, prefix="/api/chats")

MY_PROJECT = os.environ.get("MY_PROJECT", "No Project Found")
API_KEY = os.environ.get("API_KEY","Not Found")

if not API_KEY:
    raise NotImplementedError("API_KEY is not set in environment variables.")

@app.get("/")
def read_root():
    return {"Hello": "Then: World from FastAPI", "Project": MY_PROJECT}

@app.get("/health")
def health_check():
    return {"status": "healthy"}