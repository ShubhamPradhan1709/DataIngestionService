from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional

class UserCreateRequest(BaseModel):
    user_name: str
    role: str
    email: str
    mobile_no: str
    password: str

class UserCreateResponse(BaseModel):
    user_id: int
    user_name: str
    role: str
    role_id: int
    email: str
    mobile_no: str
    status_message: str 

class UserTable(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    role: str | None
    role_id: int
    user_name: str
    email: str
    status: str