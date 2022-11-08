import os

import uvicorn
from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


app.include_router(api_router)
