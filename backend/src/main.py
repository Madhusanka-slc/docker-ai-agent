from fastapi import FastAPI
import os

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT", "No Project Found")
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise NotImplementedError("API_KEY is not set in environment variables.")

@app.get("/")
def read_root():
    return {"Hello": "NEW World from FastAPI", "Project": MY_PROJECT}