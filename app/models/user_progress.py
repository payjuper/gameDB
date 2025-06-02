# app/models/user_progress.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    current_stage = Column(Integer, default=1)
    checkpoint = Column(String(255), nullable=True)
    play_time = Column(Integer, default=0)
    last_saved_at = Column(DateTime, default=func.now())
