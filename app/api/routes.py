from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import user_service
from app.db.session import get_db
from app.models.user_stats import UserStats
from app.schemas.user_stats import UserStatsCreate, UserStatsInDB
from app.models.user_progress import UserProgress
from app.schemas.user_progress import UserProgressCreate, UserProgressInDB


router = APIRouter()

# ---------------------- users ----------------------
@router.post("/users", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/users/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)

# ---------------------- user_stats ----------------------
@router.post("/user_stats/{user_id}", response_model=UserStatsInDB)
def create_user_stats(user_id: int, stats: UserStatsCreate, db: Session = Depends(get_db)):
    db_stats = UserStats(user_id=user_id, **stats.dict())
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats

@router.get("/user_stats/{user_id}", response_model=UserStatsInDB)
def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    return db.query(UserStats).filter(UserStats.user_id == user_id).first()

@router.put("/user_stats/{user_id}", response_model=UserStatsInDB)
def update_user_stats(user_id: int, stats: UserStatsCreate, db: Session = Depends(get_db)):
    db_stats = db.query(UserStats).filter(UserStats.user_id == user_id).first()
    if db_stats is None:
        raise HTTPException(status_code=404, detail="User stats not found")
    for key, value in stats.dict().items():
        setattr(db_stats, key, value)
    db.commit()
    db.refresh(db_stats)
    return db_stats
# ---------------------- user_progress ----------------------

@router.post("/user_progress/{user_id}", response_model=UserProgressInDB)
def create_user_progress(user_id: int, progress: UserProgressCreate, db: Session = Depends(get_db)):
    db_progress = UserProgress(user_id=user_id, **progress.dict())
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress

@router.get("/user_progress/{user_id}", response_model=UserProgressInDB)
def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    db_progress = db.query(UserProgress).filter(UserProgress.user_id == user_id).first()
    if db_progress is None:
        raise HTTPException(status_code=404, detail="User progress not found")
    return db_progress

@router.put("/user_progress/{user_id}", response_model=UserProgressInDB)
def update_user_progress(user_id: int, progress: UserProgressCreate, db: Session = Depends(get_db)):
    db_progress = db.query(UserProgress).filter(UserProgress.user_id == user_id).first()
    if db_progress is None:
        raise HTTPException(status_code=404, detail="User progress not found")
    for key, value in progress.dict().items():
        setattr(db_progress, key, value)
    db.commit()
    db.refresh(db_progress)
    return db_progress
