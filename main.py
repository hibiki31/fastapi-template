import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request

from database import SessionLocal, Engine, Base
from template.router import router as template_router

app = FastAPI()
app.include_router(template_router)

Base.metadata.create_all(bind=Engine)


# 全てのリクエストで同じ処理が書ける
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    # セッションを各リクエストに載せる
    request.state.db = SessionLocal()
    # 各関数で処理を行って結果を受け取る
    response = await call_next(request)
    # 結果を返す
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)