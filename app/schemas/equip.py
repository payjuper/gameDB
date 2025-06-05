from pydantic import BaseModel
from typing import Literal

class EquipRequest(BaseModel):
    user_id: int
    slot: Literal["weapon", "armor", "shield", "accessory"]
    item_id: str
