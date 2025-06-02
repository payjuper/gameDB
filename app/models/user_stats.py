from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.session import Base

class UserStats(Base):
    __tablename__ = "user_stats"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    strength = Column(Integer, default=0)
    agility = Column(Integer, default=0)
    intelligence = Column(Integer, default=0)
    luck = Column(Integer, default=0)
    morality = Column(Integer, default=0)
    life = Column(Integer, default=0)
    sanity = Column(Integer, default=0)
    hp = Column(Integer, default=1000)
    attack = Column(Integer, default=0)
    defense = Column(Integer, default=0)
    speed = Column(Integer, default=0)
    evasion = Column(Float, default=0)
    crit_rate = Column(Float, default=0)
