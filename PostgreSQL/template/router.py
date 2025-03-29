from fastapi import APIRouter, Depends
from starlette.requests import Request
from sqlalchemy.orm import Session
from database import get_db

from .models import *

router = APIRouter()

@router.get("/")
def get_index(req: Request ,db: Session = Depends(get_db)):
    return db.query(User).all()