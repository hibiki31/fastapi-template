import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request

from database import database
from template.router import router as template_router

app = FastAPI()

app.include_router(template_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)