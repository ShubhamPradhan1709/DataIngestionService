from sqlmodel import Session
from models.job import JobTable
from models.video import VideoObjectStoreResponse, VideoTable
from models.player import PlayerTable
from models.user import UserTable
from db.dbsetup import SessionDep


class PlayerCrud:
    async def create(db: SessionDep, player_data: PlayerTable):
        player = PlayerTable(**player_data.model_dump())
        db.add(player)
        db.commit()
        db.refresh(player)
        return str(player.id)

    async def get(self, db: SessionDep, player_id: str = None):
        if player_id:
            response = db.get(PlayerTable, player_id)
            return response if response else None
        
        return db.exec(PlayerTable).all()

    async def update(self, db: SessionDep, player_id: str, updated_player: PlayerTable):
        player = db.get(PlayerTable, player_id)
        if player:
            for key, value in updated_player.model_dump(exclude_unset=True).items():
                setattr(player, key, value)
            db.commit()
            db.refresh(player)
            return player
        return None

    async def delete(self, db: SessionDep, player_id: str):
        player = db.get(PlayerTable, player_id)
        if player:
            db.delete(player)
            db.commit()
            return "Player Deleted Successfully"
        return "Player not found"

player_crud = PlayerCrud()
