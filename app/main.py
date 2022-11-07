import os

import uvicorn
from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


app.include_router(api_router)


@app.get("/healthz")
async def health() -> bool:
    return True


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
