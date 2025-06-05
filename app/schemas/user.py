# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: Optional[EmailStr] = None
    created_at: datetime

    class Config:
        orm_mode = True
