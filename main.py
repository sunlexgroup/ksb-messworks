import uvicorn
from fastapi import FastAPI

from config.db import db
from config.main import settings
from apps.telegrammer.router import telegrammer_uri
from middlewares.cors_middleware import apply_cors_middleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

apply_cors_middleware(app)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(telegrammer_uri.router)


@app.get("/")
async def root():
    return {"message": "This is messanger worker"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)