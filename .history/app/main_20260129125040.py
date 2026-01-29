import os
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")