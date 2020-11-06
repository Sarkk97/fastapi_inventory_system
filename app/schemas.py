from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    email: str
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    items: List[Item] = []
    
    class Config:
        #orm_mode tells pydantic model to read the data even if it is not a dict
        #but an orm model, it can access data via attrs e.g data.id
        #making it compatible with ORMs
        orm_mode = True

class UserInDB(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str