# app/services/user_service.py
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from fastapi import HTTPException

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    user = db.query(user_model.User).filter(user_model.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user