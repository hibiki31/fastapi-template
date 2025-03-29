from fastapi_camelcase import CamelModel
from pydantic import BaseModel
from typing import List, Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserBase(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []