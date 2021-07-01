import uvicorn
from fastapi import FastAPI

from config.db import db
from apps.telegrammer.router import telegrammer_uri


app = FastAPI(title="Async FastAPI")


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(telegrammer_uri.router)

@app.get("")
async def root():
    return {"message": "This is telegram worker"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)