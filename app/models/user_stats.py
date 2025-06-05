from sqlalchemy import Column, Integer, Float, Text, ForeignKey
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
    spirit = Column(Integer, default=0)
    experience = Column(Integer, default=0)
    level = Column(Integer, default=1)
    equipped_items = Column(Text)         # 예: {"weapon": "sword_id", ...}
    inventory_items = Column(Text)        # 예: ["item1", "item2", ...]
    
