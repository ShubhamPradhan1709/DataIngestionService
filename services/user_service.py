from sqlmodel import Session
from models.job import JobTable
from models.video import VideoObjectStoreResponse, VideoTable
from models.player import PlayerTable
from models.user import UserTable
from db.dbsetup import SessionDep
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

class UserCrud:
    async def create(self, db: SessionDep, user_data: UserTable):
        user = UserTable(**user_data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return str(user.id)

    async def get(self, db: SessionDep, user_id: str = None):
        if user_id:
            response = db.get(UserTable, user_id)
            return response if response else None
        
        return db.exec(UserTable).all()

    async def update(self, db: SessionDep, user_id: str, updated_user: UserTable):
        user = db.get(UserTable, user_id)
        if user:
            for key, value in updated_user.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
            return user
        return None

    async def delete(self, db: SessionDep, user_id: str):
        user = db.get(UserTable, user_id)
        if user:
            db.delete(user)
            db.commit()
            return "User Deleted Successfully"
        return "User not found"

user_crud = UserCrud()


