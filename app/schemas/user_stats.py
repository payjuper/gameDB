from pydantic import BaseModel

class UserStatsBase(BaseModel):
    strength: int = 0
    agility: int = 0
    intelligence: int = 0
    luck: int = 0
    morality: int = 0
    life: int = 0
    sanity: int = 0
    hp: int = 1000
    attack: int = 0
    defense: int = 0
    speed: int = 0
    evasion: float = 0.0
    crit_rate: float = 0.0

class UserStatsCreate(UserStatsBase):
    pass

class UserStatsInDB(UserStatsBase):
    user_id: int

    class Config:
        orm_mode = True
