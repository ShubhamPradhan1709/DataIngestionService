from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional, Dict

class PlayerRequest(BaseModel):
    player_id: int
    player_name: str
    player_no: int
    position: str


class PlayerResponse(BaseModel):
    player_id: int
    player_name: str
    # stats: Optional[Dict] 

class PlayerTable(SQLModel, table=True):
    player_id: Optional[int] = Field(default=None, primary_key=True)
    player_name: str
    position: str
    # stats: Optional[Dict]