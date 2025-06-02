# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None
    level: Optional[int] = 1
    experience: Optional[int] = 0

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: Optional[EmailStr] = None
    level: int
    experience: int
    created_at: datetime

    class Config:
        orm_mode = True
