import os
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "dev")

@app.get("/health")
def health_check():
    return {"Status": "OK", "Version": APP_VERSION}