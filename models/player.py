from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class PlayerRequest(BaseModel):
    player_id: int
    player_name: str
    player_no: int
    position: str


class PlayerResponse(BaseModel):
    player_id: int
    player_name: str
    stats: dict 

class PlayerTable(SQLModel, table=True):
    player_id: int = Field(default=None, primary_key=True)
    player_name: str
    position: str
    stats: dict