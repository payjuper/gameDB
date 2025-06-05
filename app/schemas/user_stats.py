from pydantic import BaseModel
from typing import Dict, Optional, List

class UserStatsBase(BaseModel):
    strength: int = 0
    agility: int = 0
    intelligence: int = 0
    luck: int = 0
    morality: int = 0
    life: int = 0
    spirit: int = 0            # ✅ 새로 추가
    experience: int = 0        # ✅ 새로 추가
    level: int = 1             # ✅ 새로 추가
    equipped_items: Dict[str, Optional[str]] = {
        "weapon": None,
        "armor": None,
        "shield": None,
        "accessory": None
    }
    inventory_items: List[str] = []

class UserStatsCreate(UserStatsBase):
    pass

class UserStatsInDB(UserStatsBase):
    user_id: int

    class Config:
        orm_mode = True
