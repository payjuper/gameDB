# app/schemas/user_progress.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserProgressBase(BaseModel):
    current_stage: int = 1
    checkpoint: Optional[str] = None
    play_time: int = 0

class UserProgressCreate(UserProgressBase):
    pass

class UserProgressInDB(UserProgressBase):
    user_id: int
    last_saved_at: datetime

    class Config:
        from_attributes = True
