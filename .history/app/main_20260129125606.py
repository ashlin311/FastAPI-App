import os
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = os.getenv("A", "dev")

@app.get("/health")
def health_check():
    return {"Status": "OK"}

@app.get("/version")
def get_version():
    return {"version": APP_VERSION}